# Generated by Django 4.2.6 on 2023-10-31 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_id',
            field=models.CharField(max_length=100),
        ),
    ]