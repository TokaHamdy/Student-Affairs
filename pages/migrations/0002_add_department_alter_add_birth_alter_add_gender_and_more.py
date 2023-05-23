# Generated by Django 4.0.4 on 2022-05-17 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='add',
            name='department',
            field=models.CharField(choices=[('cs', 'computer science'), ('is', 'Information System'), ('ai', 'Artificial Intelligence'), ('it', 'Information Technology'), ('ds', 'Operations Research and Decision Support'), ('none', 'None')], default='', max_length=30, verbose_name='Department'),
        ),
        migrations.AlterField(
            model_name='add',
            name='birth',
            field=models.DateField(verbose_name='Birthday'),
        ),
        migrations.AlterField(
            model_name='add',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=30, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='add',
            name='phoneNumber',
            field=models.PositiveBigIntegerField(default=' ', unique=True, verbose_name='Phone Number '),
        ),
    ]
