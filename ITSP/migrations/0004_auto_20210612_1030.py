# Generated by Django 3.2.4 on 2021-06-12 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ITSP', '0003_auto_20210612_1030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teamdata',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='teamdata',
            name='published_date',
        ),
    ]
