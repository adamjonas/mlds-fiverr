from .models import *
import django_filters

class PrOutPositionFilter(django_filters.FilterSet):
	class Meta:
		model = PrOutPosition
		fields = ['position', 'year', 'value', ]


class PrOutStatusFilter(django_filters.FilterSet):
	class Meta:
		model = PrOutStatus
		fields = ['status', 'year', 'value', ]