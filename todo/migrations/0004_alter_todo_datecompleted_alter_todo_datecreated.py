# Generated by Django 4.0.3 on 2022-03-14 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_alter_todo_datecreated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='datecompleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='datecreated',
            field=models.DateField(auto_now_add=True),
        ),
    ]
