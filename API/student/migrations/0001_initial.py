# Generated by Django 4.2.6 on 2023-10-21 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('parentsName', models.CharField(max_length=50)),
                ('dOb', models.DateField()),
                ('favSubject', models.CharField(max_length=50)),
            ],
        ),
    ]
