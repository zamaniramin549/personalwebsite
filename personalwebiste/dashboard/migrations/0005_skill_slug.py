# Generated by Django 4.0.3 on 2022-03-19 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_skill_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='slug',
            field=models.SlugField(default='html', unique=True),
            preserve_default=False,
        ),
    ]
