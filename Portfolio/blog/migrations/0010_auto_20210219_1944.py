# Generated by Django 3.1.6 on 2021-02-19 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20210219_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, default='coding', null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.category'),
        ),
    ]