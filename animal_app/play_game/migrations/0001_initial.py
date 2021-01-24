# Generated by Django 3.1.5 on 2021-01-24 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('name', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('population', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('image_license', models.CharField(max_length=200)),
                ('license_url', models.CharField(max_length=200)),
                ('image_url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
