# Generated by Django 4.1.7 on 2023-07-17 02:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('note', '0012_remove_audio_note_audio_id_audio_note_note_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio_note',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
