# Generated by Django 3.1.6 on 2021-02-24 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('linkList', '0002_auto_20210212_0026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='linklist',
            old_name='tags',
            new_name='linkTags',
        ),
    ]
