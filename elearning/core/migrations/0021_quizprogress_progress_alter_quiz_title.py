# Generated by Django 5.1 on 2024-09-26 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_contentprogress_viewed'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizprogress',
            name='progress',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
