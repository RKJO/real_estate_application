# Generated by Django 2.1.2 on 2018-11-26 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]