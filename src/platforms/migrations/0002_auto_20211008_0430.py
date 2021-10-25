# Generated by Django 2.2.13 on 2021-10-08 04:30

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('platforms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='platforms',
            name='croppingLogo',
            field=image_cropping.fields.ImageRatioField('logo', '600x400', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='croppingLogo'),
        ),
        migrations.AddField(
            model_name='platforms',
            name='croppingProfileImage',
            field=image_cropping.fields.ImageRatioField('profileImage', '1100x400', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='croppingProfileImage'),
        ),
        migrations.AlterField(
            model_name='platforms',
            name='logo',
            field=image_cropping.fields.ImageCropField(blank=True, max_length=300, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='platforms',
            name='profileImage',
            field=image_cropping.fields.ImageCropField(blank=True, max_length=300, null=True, upload_to='images/'),
        ),
    ]