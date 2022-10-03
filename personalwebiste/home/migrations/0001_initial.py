# Generated by Django 4.0.3 on 2022-03-26 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0011_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('blog_pk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.blog')),
            ],
        ),
    ]