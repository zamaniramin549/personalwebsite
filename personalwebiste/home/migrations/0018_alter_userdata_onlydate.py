# Generated by Django 4.0.3 on 2022-05-07 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_userdata_device_family'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='onlydate',
            field=models.DateField(auto_now=True),
        ),
    ]