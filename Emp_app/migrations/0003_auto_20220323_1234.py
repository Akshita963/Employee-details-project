# Generated by Django 3.0 on 2022-03-23 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Emp_app', '0002_auto_20220322_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='empCategory',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='empCity',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='empDescription',
            field=models.CharField(max_length=250),
        ),
    ]