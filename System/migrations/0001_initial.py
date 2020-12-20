# Generated by Django 3.1.3 on 2020-12-19 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Email', models.EmailField(default='', max_length=254)),
                ('Password', models.CharField(max_length=20)),
                ('Confirm_Password', models.CharField(max_length=20)),
            ],
        ),
    ]
