# Generated by Django 3.1.2 on 2020-10-25 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20201022_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_bio',
            field=models.TextField(max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_photo',
            field=models.ImageField(null=True, upload_to='profile-photo'),
        ),
    ]
