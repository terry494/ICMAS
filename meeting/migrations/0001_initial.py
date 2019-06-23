# Generated by Django 2.2.2 on 2019-06-23 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Park',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modify_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('floor', models.CharField(max_length=20)),
                ('capacity', models.CharField(max_length=20)),
                ('equipment', models.CharField(max_length=20)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modify_date', models.DateTimeField(auto_now_add=True)),
                ('parks_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meeting.Park')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=20)),
                ('creator', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=50)),
                ('corp', models.CharField(max_length=20)),
                ('order_date', models.DateTimeField(max_length=20)),
                ('start_time', models.DateTimeField(max_length=20)),
                ('end_time', models.DateTimeField(max_length=20)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modify_date', models.DateTimeField(auto_now_add=True)),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meeting.Room')),
            ],
        ),
    ]
