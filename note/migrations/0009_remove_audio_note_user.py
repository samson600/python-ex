# Generated by Django 4.1.7 on 2023-06-27 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0008_rename_user_id_audio_note_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audio_note',
            name='user',
        ),
    ]
