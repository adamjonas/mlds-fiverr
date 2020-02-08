from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.views.generic.base import TemplateView
from django.views.decorators.csrf import csrf_exempt

from .models import *
from .acefs import *

import datetime
import hashlib
import base64
import time
import random

import os


def _hash_helper(input):
	password_salt = os.urandom(32).hex()
	h = hashlib.sha256()
	h.update(('%s%s' % (password_salt, input)).encode('utf-8'))
	h.update(('%s%s' % (password_salt, settings.SECRET)).encode('utf-8'))
	return h.hexdigest()


def _get_or_create_visitor(request):

	if request.GET.get('skip_log', False):
		return None

	user_agent = request.META['HTTP_USER_AGENT']

	bots = ['Pingdom.com_bot_']
	for b in bots:
		if user_agent.startswith(b):
			return None

	visitor = None
	try:
		visitor_id = request.session['visitor_id']
		visitor = Visitor.objects.get(pk=visitor_id)

	except Exception as e:
		visitor = Visitor()
		visitor.save()
		request.session['visitor_id']= visitor.id

	# Update IP and User-Agent
	visitor.ip = request.META.get('HTTP_X_REAL_IP', None) # Set by NGINX
	if not visitor.ip:
		visitor.ip = request.META['REMOTE_ADDR']
	visitor.user_agent = user_agent
	visitor.save()

	return visitor


def backdoor(request):

	visitor = _get_or_create_visitor(request)
	if visitor:
		visitor.username = '--'
		visitor.fullname = '(Backdoor User)'
		visitor.save()
	
	salt = str(random.randrange(10000,10000000))
	hash = _hash_helper(salt)

	response = HttpResponseRedirect('/')
	response.set_cookie('salt', salt, 365*24*60*60)
	response.set_cookie('hash', hash, 365*24*60*60)
	return response


def main(request):

	visitor = _get_or_create_visitor(request)

	colleges = College.objects.all().order_by('school')
	occupations = DOLSalary.objects.all().order_by('occupation')
	draft_cells = DRAFT_CELLS
	positions = POSITIONS
	statuses = STATUSES

	if request.method == 'POST':

		# We might have a token from the other server:

		encoded = request.POST['encoded']
		hashed = request.POST['hashed']

		other_t = base64.b64decode(encoded)
		this_t = time.time()

		delta = abs(int(other_t) - this_t)

		this_hash = _hash_helper(other_t)

		if (delta > (60*60*2)) or (hashed != this_hash):

			return render(request, 'auth_error.html', context) 

		else:

			salt = str(random.randrange(10000,10000000))
			hash = _hash_helper(salt)

			# Save User Data to Session
			if visitor:
				visitor.modx_id = request.POST['id']
				visitor.username = request.POST['username']
				visitor.fullname = request.POST['fullname']
				visitor.save()

			response = HttpResponseRedirect('/')
			response.set_cookie('salt', salt, 365*24*60*60)
			response.set_cookie('hash', hash, 365*24*60*60)
			return response

	context = {
		'colleges': colleges,
		'occupations': occupations,
		'draft_cells': draft_cells,
		'positions': positions,
		'statuses': 'statuses',
	}
	
	return render(request, 'index.html', context) 

@csrf_exempt
def output(request):

	college = request.POST.get('college')
	alt = request.POST.get('alt')
	sec = request.POST.get('sec')
	pick = request.POST.get('pick')
	pos = request.POST.get('pos')
	status = request.POST.get('status')

	acefsm = AcefsModel(college=college, alt=alt, secondary=sec, expected_pick=pick, position=pos, status=status)

	visitor = _get_or_create_visitor(request)

	if visitor:
		scenario = Scenario()
		scenario.visitor = visitor
		scenario.college = acefsm.college
		scenario.alt = acefsm.alt
		scenario.sec = acefsm.secondary
		scenario.pick = acefsm.expected_pick.cell
		scenario.pos = acefsm.position.index
		scenario.status = acefsm.status.index
		scenario.save()

	# We might have a cookie:
	salt = request.COOKIES.get('salt', '')
	hash = request.COOKIES.get('hash', '')

	context = {
		'salt': salt,
		'hash': hash,
	}

#	if 'salt' in request.COOKIES:
#		if (hash != _hash_helper(salt)):
#			return render(request, 'auth_error.html', context) 
#	else:
#		return render(request, 'auth_error.html', context)

	if visitor:
		scenario.anonymous = False
		scenario.save()

	table = []
	for y in range(0, TOTAL_YEARS):
		table.append({
			'year': y + datetime.datetime.now().year,
			'pr_minors': acefsm.pr_minors[y],
			'pr_out': acefsm.pr_out[y]
		})

	this_year = datetime.datetime.now().year
	graph = [
		{
			'label': 'Earnings [Baseball]',
			'data': [[y + this_year, acefsm.e_mlb[y]] for y in range(0, TOTAL_YEARS)],
			'color': '#009900'
		},
		{
			'label': 'Earnings [Alternate]',
			'data': [[y + this_year, acefsm.e_alt[y]] for y in range(0, TOTAL_YEARS)],
			'color': '#CC0000'
		}

		]

	years = [this_year + 2 * y + 1 for y in range(0, TOTAL_YEARS//2)]

	context = {
		'model': acefsm,
		'table': table,
		'graph': graph,
		'years': years,
	}

	return render(request, 'output.html', context) 

@staff_member_required
def visitors(request):
	context = {
	}
	return render(request, 'visitors.html', context) 

@staff_member_required
def visitor_list(request, page_num=1):

	# Annotate using number of scenarios and filter to show only > 0
	visitors = Visitor.objects.annotate(num_scenarios=Count('scenario'))
	visitors = visitors.filter(num_scenarios__gt=0).order_by('id')

	if 'term' in request.GET:
		term = request.GET['term']
		visitors = visitors.filter(fullname__icontains=term)
	
	else:
		term = ''
		visitors = visitors.all()

	paginator = Paginator(visitors, 20)
	page = paginator.get_page(page_num)

	context = {
		'term': term,
		'page': page,
	}

	return render(request, 'visitor_list.html', context) 

@staff_member_required
def visitor_detail(request, visitor_id):
	context = {
		'visitor': Visitor.objects.get(pk=visitor_id)
	}

	return render(request, 'visitor_detail.html', context) 
