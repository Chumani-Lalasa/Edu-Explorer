# Generated by Django 5.1 on 2024-10-03 07:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_content_video_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='module',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.module'),
        ),
    ]
