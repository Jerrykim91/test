# Generated by Django 3.1.4 on 2021-01-20 14:55

from django.db import migrations, models
import django.db.models.deletion
import melog.fields


class Migration(migrations.Migration):

    dependencies = [
        ('melog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=100, verbose_name='One Line Description')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='TITLE')),
                ('description', models.TextField(blank=True, verbose_name='Photo Description')),
                ('image', melog.fields.ThumbnailImageField(upload_to='melog/%y/%m')),
                ('upload_dt', models.DateTimeField(auto_now_add=True, verbose_name='Upload Date')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='melog.album')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.DeleteModel(
            name='Melog',
        ),
    ]
