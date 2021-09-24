# Generated by Django 3.2.7 on 2021-09-23 16:58

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20210921_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='file_field_name',
            field=models.FileField(blank=True, max_length=254, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='article',
            name='img_field_name',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
