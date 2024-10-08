# Generated by Django 5.1 on 2024-08-23 11:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_module_order_courseprogress_questionanswer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='difficulty',
            field=models.CharField(choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')], default='medium', max_length=50),
        ),
        migrations.AddField(
            model_name='quizprogress',
            name='feedback',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='content_type',
            field=models.CharField(choices=[('video', 'Video'), ('article', 'Article'), ('quiz', 'Quiz'), ('file', 'File')], max_length=50),
        ),
        migrations.AlterField(
            model_name='questionanswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_answers_list', to='core.question'),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('is_correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers_list', to='core.question')),
            ],
        ),
    ]
