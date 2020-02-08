# Generated by Django 3.0.3 on 2020-02-08 03:24

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('starting', models.IntegerField()),
                ('mid_career', models.IntegerField()),
                ('start_fx', models.FloatField()),
                ('mid_fx', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'Colleges',
            },
        ),
        migrations.CreateModel(
            name='DOLSalary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occupation', models.CharField(max_length=255)),
                ('sal10', models.IntegerField()),
                ('sal25', models.IntegerField()),
                ('sal50', models.IntegerField()),
                ('sal75', models.IntegerField()),
                ('sal90', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'DOLSalaries',
            },
        ),
        migrations.CreateModel(
            name='MLBData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(choices=[(0, 'C'), (1, '1B-DH'), (2, '2B'), (3, '3B'), (4, 'SS'), (5, 'OF'), (6, 'LHP'), (7, 'RHP'), (8, 'ALL')], validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(8)])),
                ('status', models.IntegerField(choices=[(0, 'HS'), (1, 'JC'), (2, '4YR')], validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)])),
                ('draft_cell', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(26)])),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(19)])),
                ('value', models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)])),
            ],
            options={
                'verbose_name_plural': 'MLBData',
            },
        ),
        migrations.CreateModel(
            name='PrMajorsData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(choices=[(0, 'C'), (1, '1B-DH'), (2, '2B'), (3, '3B'), (4, 'SS'), (5, 'OF'), (6, 'LHP'), (7, 'RHP'), (8, 'ALL')], validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(8)])),
                ('status', models.IntegerField(choices=[(0, 'HS'), (1, 'JC'), (2, '4YR')], validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)])),
                ('draft_cell', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(26)])),
                ('value', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)])),
            ],
            options={
                'verbose_name_plural': 'PrMajorsData',
            },
        ),
        migrations.CreateModel(
            name='PrOutPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(choices=[(0, 'C'), (1, '1B-DH'), (2, '2B'), (3, '3B'), (4, 'SS'), (5, 'OF'), (6, 'LHP'), (7, 'RHP'), (8, 'ALL')], validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(8)])),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(18)])),
                ('value', models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)])),
            ],
            options={
                'verbose_name_plural': 'PrOutPositions',
            },
        ),
        migrations.CreateModel(
            name='PrOutStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'HS'), (1, 'JC'), (2, '4YR')], validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)])),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(18)])),
                ('value', models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)])),
            ],
            options={
                'verbose_name_plural': 'PrOutStatuses',
            },
        ),
        migrations.CreateModel(
            name='SigningBonus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('draft_cell', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(26)])),
                ('status', models.IntegerField(choices=[(0, 'HS'), (1, 'JC'), (2, '4YR')], validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)])),
                ('amount', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'SigningBonuses',
            },
        ),
        migrations.CreateModel(
            name='SlotBonus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pick', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('draft_cell', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(26)])),
            ],
            options={
                'verbose_name_plural': 'SlotBonuses',
            },
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modx_id', models.IntegerField(blank=True, null=True)),
                ('username', models.CharField(blank=True, max_length=64, null=True)),
                ('fullname', models.CharField(blank=True, max_length=64, null=True)),
                ('ip', models.CharField(max_length=15)),
                ('user_agent', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Scenario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('anonymous', models.BooleanField(default=True)),
                ('pick', models.IntegerField()),
                ('pos', models.IntegerField(blank=True, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('alt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alt_scenario_set', to='acefs.DOLSalary')),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acefs.College')),
                ('sec', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sec_scenario_set', to='acefs.DOLSalary')),
                ('visitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acefs.Visitor')),
            ],
        ),
    ]
