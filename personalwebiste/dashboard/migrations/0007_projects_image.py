# Generated by Django 4.0.3 on 2022-03-20 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_projects_alter_about_options_alter_skill_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='image',
            field=models.FileField(default='test', upload_to='projects/'),
            preserve_default=False,
        ),
    ]
