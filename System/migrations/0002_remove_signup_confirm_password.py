# Generated by Django 3.1.3 on 2020-12-19 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('System', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='Confirm_Password',
        ),
    ]