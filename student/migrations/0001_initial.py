# Generated by Django 4.0.4 on 2022-05-23 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Add',
            fields=[
                ('student_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('GPA', models.DecimalField(decimal_places=2, max_digits=3)),
                ('level', models.IntegerField()),
                ('birthday', models.DateField()),
                ('department', models.CharField(choices=[('None', 'None'), ('Computer science', 'Computer science'), ('Operations Research and Decision Support', 'Operations Research and Decision Support'), ('Information System', 'Information System'), ('Information Technology', 'Information Technology'), ('Artificial intelligence', 'Artificial intelligence')], max_length=50)),
                ('phonenumber', models.CharField(max_length=12)),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=8)),
                ('State', models.CharField(choices=[('Active', 'Active'), ('InActive', 'InActive')], max_length=8)),
            ],
        ),
    ]
