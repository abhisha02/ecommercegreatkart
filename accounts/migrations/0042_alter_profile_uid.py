# Generated by Django 4.2.9 on 2024-02-09 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0041_alter_profile_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='uid',
            field=models.CharField(default='<function uuid4 at 0x00000182A9F8BEC0>', max_length=200),
        ),
    ]
