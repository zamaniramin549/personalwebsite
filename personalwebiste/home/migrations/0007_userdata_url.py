# Generated by Django 4.0.3 on 2022-05-06 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_userdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='url',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]