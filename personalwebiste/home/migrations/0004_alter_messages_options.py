# Generated by Django 4.0.3 on 2022-03-27 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_messages_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='messages',
            options={'ordering': ('-date',), 'verbose_name_plural': 'Messages'},
        ),
    ]