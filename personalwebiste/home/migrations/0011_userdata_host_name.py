# Generated by Django 4.0.3 on 2022-05-07 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_userdata_operating_system'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='host_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
