# Generated by Django 4.0.3 on 2022-05-07 12:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_userdata_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='onlydate',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
