# Generated by Django 4.0.3 on 2022-03-31 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_resumeprofessionalskill'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResumeWorkExpe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Resume work experience',
            },
        ),
    ]
