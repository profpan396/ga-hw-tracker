# Generated by Django 3.2.6 on 2021-10-26 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_alter_todo_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.DateField(max_length=100),
        ),
        migrations.AlterField(
            model_name='todo',
            name='time',
            field=models.TimeField(max_length=12),
        ),
    ]
