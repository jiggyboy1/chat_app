# Generated by Django 5.0.1 on 2024-03-11 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_message_options_alter_room_options_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='address',
            new_name='location',
        ),
    ]
