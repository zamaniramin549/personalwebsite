# Generated by Django 4.0.3 on 2022-03-27 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_resumeabout'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResumeTechnicalSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.TextField(blank=True, null=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Resume Technical Skills',
            },
        ),
    ]
