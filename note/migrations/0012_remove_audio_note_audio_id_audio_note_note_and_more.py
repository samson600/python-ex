# Generated by Django 4.1.7 on 2023-07-17 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0011_rename_user_id_audio_note_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audio_note',
            name='audio_id',
        ),
        migrations.AddField(
            model_name='audio_note',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='audio_note',
            name='audio',
            field=models.CharField(max_length=100),
        ),
    ]