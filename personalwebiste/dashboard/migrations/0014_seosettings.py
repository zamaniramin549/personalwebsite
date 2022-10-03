# Generated by Django 4.0.3 on 2022-05-01 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_navbarsetting_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeoSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('keywords', models.TextField(blank=True)),
                ('sitename', models.CharField(blank=True, max_length=255)),
                ('image', models.FileField(blank=True, upload_to='image/')),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'SEO setting',
            },
        ),
    ]