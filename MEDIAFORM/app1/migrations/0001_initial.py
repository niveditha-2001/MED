# Generated by Django 5.0.2 on 2024-02-20 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mname', models.CharField(max_length=20)),
                ('mdirector', models.CharField(max_length=20)),
                ('mposter', models.ImageField(upload_to='gallery')),
            ],
        ),
    ]
