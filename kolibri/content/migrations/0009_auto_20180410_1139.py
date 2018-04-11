# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-10 18:39
from __future__ import unicode_literals

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0008_contentnode_coach_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='preset',
            field=models.CharField(blank=True, choices=[('high_res_video', 'High Resolution'), ('low_res_video', 'Low Resolution'), ('vector_video', 'Vectorized'), ('video_thumbnail', 'Thumbnail'), ('video_subtitle', 'Subtitle'), ('audio', 'Audio'), ('audio_thumbnail', 'Thumbnail'), ('document', 'Document'), ('epub', 'ePub Document'), ('document_thumbnail', 'Thumbnail'), ('exercise', 'Exercise'), ('exercise_thumbnail', 'Thumbnail'), ('exercise_image', 'Exercise Image'), ('exercise_graphie', 'Exercise Graphie'), ('channel_thumbnail', 'Channel Thumbnail'), ('topic_thumbnail', 'Thumbnail'), ('html5_zip', 'HTML5 Zip'), ('html5_thumbnail', 'HTML5 Thumbnail')], max_length=150),
        ),
        migrations.AlterField(
            model_name='localfile',
            name='extension',
            field=models.CharField(blank=True, choices=[('mp4', 'MP4 Video'), ('vtt', 'VTT Subtitle'), ('srt', 'SRT Subtitle'), ('mp3', 'MP3 Audio'), ('pdf', 'PDF Document'), ('jpg', 'JPG Image'), ('jpeg', 'JPEG Image'), ('png', 'PNG Image'), ('gif', 'GIF Image'), ('json', 'JSON'), ('svg', 'SVG Image'), ('perseus', 'Perseus Exercise'), ('zip', 'HTML5 Zip'), ('epub', 'ePub Document')], max_length=40),
        ),
    ]