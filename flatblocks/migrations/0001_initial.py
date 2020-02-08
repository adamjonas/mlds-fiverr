# Generated by Django 3.0.3 on 2020-02-08 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FlatBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(help_text='A unique name used for reference in the templates', max_length=255, unique=True, verbose_name='Slug')),
                ('header', models.CharField(blank=True, help_text='An optional header for this content', max_length=255, verbose_name='Header')),
                ('content', models.TextField(blank=True, verbose_name='Content')),
            ],
            options={
                'verbose_name': 'Flat block',
                'verbose_name_plural': 'Flat blocks',
            },
        ),
    ]
