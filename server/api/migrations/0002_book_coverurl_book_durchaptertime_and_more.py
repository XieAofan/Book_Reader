# Generated by Django 4.1.5 on 2023-01-24 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='coverUrl',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='book',
            name='durChapterTime',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='book',
            name='durChapterindex',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=5),
        ),
        migrations.AddField(
            model_name='book',
            name='durChaptertitle',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='book',
            name='latestChapterTime',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='book',
            name='latestChaptertindex',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=5),
        ),
        migrations.AddField(
            model_name='book',
            name='latestChaptertitle',
            field=models.CharField(default='', max_length=200),
        ),
    ]