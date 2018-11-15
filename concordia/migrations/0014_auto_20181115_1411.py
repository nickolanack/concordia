# Generated by Django 2.0.9 on 2018-11-15 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("concordia", "0013_auto_20181031_1305")]

    operations = [
        migrations.AlterField(
            model_name="asset",
            name="transcription_status",
            field=models.CharField(
                choices=[
                    ("not_started", "Not Started"),
                    ("in_progress", "In Progress"),
                    ("submitted", "Submitted for Review"),
                    ("completed", "Completed"),
                ],
                default="not_started",
                editable=False,
                max_length=20,
            ),
        )
    ]
