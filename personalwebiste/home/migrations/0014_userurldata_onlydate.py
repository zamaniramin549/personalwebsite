# Generated by Django 4.0.3 on 2022-05-07 13:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_userdata_onlydate'),
    ]

    operations = [
        migrations.AddField(
            model_name='userurldata',
            name='onlydate',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]