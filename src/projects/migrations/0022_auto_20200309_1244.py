# Generated by Django 2.2.10 on 2020-03-09 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0021_auto_20200306_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image2',
            field=models.ImageField(blank=True, max_length=300, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='project',
            name='image3',
            field=models.ImageField(blank=True, max_length=300, null=True, upload_to='images/'),
        ),
    ]