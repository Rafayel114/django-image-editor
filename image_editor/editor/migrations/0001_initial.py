# Generated by Django 3.0.8 on 2020-07-29 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, upload_to='Images/files')),
                ('img_url', models.URLField(blank=True, default='')),
            ],
        ),
    ]
