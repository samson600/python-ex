# Generated by Django 4.1.7 on 2023-06-27 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0004_rename_neme_users_name_alter_audio_note_audio_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio_note',
            name='audio_id',
            field=models.CharField(max_length=150),
        ),
    ]