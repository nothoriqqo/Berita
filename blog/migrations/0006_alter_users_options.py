# Generated by Django 4.1.1 on 2022-12-17 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_users_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name_plural': 'Users'},
        ),
    ]
