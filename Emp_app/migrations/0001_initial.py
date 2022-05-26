# Generated by Django 4.0.3 on 2022-03-21 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('empID', models.AutoField(primary_key=True, serialize=False)),
                ('empName', models.CharField(max_length=100)),
                ('empDescription', models.CharField(blank=True, max_length=250)),
                ('empCategory', models.CharField(blank=True, max_length=100)),
                ('empCity', models.CharField(max_length=50)),
            ],
        ),
    ]