# Generated by Django 3.1.2 on 2020-10-22 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201017_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='paypal_donate',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
