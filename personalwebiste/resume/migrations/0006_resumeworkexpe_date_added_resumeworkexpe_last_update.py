# Generated by Django 4.0.3 on 2022-03-31 06:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_resumeworkexpe'),
    ]

    operations = [
        migrations.AddField(
            model_name='resumeworkexpe',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resumeworkexpe',
            name='last_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
