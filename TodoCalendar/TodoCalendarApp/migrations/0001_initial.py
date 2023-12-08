# Generated by Django 4.2.4 on 2023-12-07 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Labels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('labels', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskName', models.CharField(max_length=30)),
                ('taskDescription', models.TextField()),
                ('openDate', models.DateTimeField(auto_now_add=True)),
                ('dueDate', models.DateTimeField()),
                ('completed', models.BooleanField(default=False)),
                ('label', models.ManyToManyField(to='TodoCalendarApp.labels')),
            ],
        ),
    ]
