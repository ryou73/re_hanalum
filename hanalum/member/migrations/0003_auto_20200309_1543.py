# Generated by Django 3.0.2 on 2020-03-09 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_auto_20200309_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='admission_year',
            field=models.IntegerField(default=1, verbose_name='Admission_year'),
        ),
        migrations.AlterField(
            model_name='user',
            name='authority',
            field=models.IntegerField(default=1, verbose_name='Authority'),
        ),
    ]