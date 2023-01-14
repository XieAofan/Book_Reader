# Generated by Django 4.1.2 on 2023-01-13 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('source', models.JSONField()),
                ('current_source', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('site_name', models.CharField(max_length=200)),
                ('site_url', models.CharField(max_length=200)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('site_strategy', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usrename', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('bookshelf', models.JSONField()),
            ],
        ),
    ]
