# Generated by Django 2.2.12 on 2020-04-13 13:24

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textblock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='textblock',
            name='body_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(help_text='Texto del bloque en inglés', null=True, verbose_name='Texto inglés'),
        ),
    ]