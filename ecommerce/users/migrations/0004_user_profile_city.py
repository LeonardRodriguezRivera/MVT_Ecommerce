# Generated by Django 4.0.6 on 2022-08-28 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_profile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='city',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]
