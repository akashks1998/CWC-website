# Generated by Django 2.0.6 on 2018-07-19 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cwc', '0002_auto_20180717_1241'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('club', models.CharField(max_length=20)),
                ('title', models.TextField(max_length=500)),
            ],
        ),
    ]
