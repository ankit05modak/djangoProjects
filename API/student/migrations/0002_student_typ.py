# Generated by Django 4.2.6 on 2023-10-21 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='typ',
            field=models.CharField(default='Regular', max_length=10),
        ),
    ]
