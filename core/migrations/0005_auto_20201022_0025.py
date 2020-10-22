# Generated by Django 3.1.2 on 2020-10-22 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20201021_2341'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(blank=True, default=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='video',
            name='likes',
        ),
    ]
