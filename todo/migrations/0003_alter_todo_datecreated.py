# Generated by Django 4.0.3 on 2022-03-14 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_todo_datecompleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='datecreated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
