# Generated by Django 3.1.2 on 2020-10-22 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20201022_1157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='paypal_url_to_receive_donation',
        ),
    ]