# Generated by Django 4.0.3 on 2022-05-14 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_alter_userdata_onlydate'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='seen',
            field=models.BooleanField(default=True),
        ),
    ]
