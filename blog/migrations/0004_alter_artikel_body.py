# Generated by Django 4.1.1 on 2022-12-17 05:35

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_berita_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikel',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
