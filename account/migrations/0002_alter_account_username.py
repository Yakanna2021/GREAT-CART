# Generated by Django 4.2.3 on 2023-07-19 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
