# Generated by Django 4.0.4 on 2022-05-23 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add',
            name='birthday',
            field=models.DateField(default=0),
        ),
    ]