# Generated by Django 4.1.7 on 2023-06-27 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0006_audio_note_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='audio_note',
            old_name='user',
            new_name='user_id',
        ),
    ]