# Generated by Django 3.1.6 on 2021-02-19 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20210220_0344'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='photo_Art',
            new_name='image',
        ),
    ]