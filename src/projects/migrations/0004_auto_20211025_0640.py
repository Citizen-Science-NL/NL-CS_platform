# Generated by Django 2.2.13 on 2021-10-25 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_moderated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='participationtask',
            new_name='participationTask',
        ),
    ]