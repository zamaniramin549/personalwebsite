# Generated by Django 4.0.3 on 2022-04-12 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0008_resumeeducation'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResumeAwards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('award', models.CharField(max_length=100)),
                ('award_title', models.CharField(max_length=100)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Resume awards',
            },
        ),
    ]
