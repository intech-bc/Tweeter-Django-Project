# Generated by Django 3.0.7 on 2020-07-21 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20200721_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweets',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]