# Generated by Django 5.0.6 on 2024-06-19 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskrecord',
            name='date_completed',
            field=models.DateField(),
        ),
    ]
