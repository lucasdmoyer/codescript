# Generated by Django 5.0.7 on 2024-07-11 21:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0002_remove_submission_analysis_remove_submission_score_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('analysis', models.TextField()),
                ('score', models.IntegerField(blank=True, choices=[(1, 'Incorrect'), (2, 'Partially Correct'), (3, 'Correct')], null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='response', to='api.submission')),
            ],
        ),
    ]
