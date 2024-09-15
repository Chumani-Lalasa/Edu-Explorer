# Generated by Django 5.1 on 2024-09-15 15:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_question_correct_answer_alter_question_quiz_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='correct_answer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='correct_for_question', to='core.answer'),
        ),
    ]
