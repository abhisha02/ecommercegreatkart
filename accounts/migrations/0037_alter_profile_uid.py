# Generated by Django 4.2.9 on 2024-01-27 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0036_alter_profile_uid_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='uid',
            field=models.CharField(default='<function uuid4 at 0x000001D87E3ABEC0>', max_length=200),
        ),
    ]
