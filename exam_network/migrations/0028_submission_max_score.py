# Generated by Django 3.0.7 on 2021-04-05 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_network', '0027_submission_percentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='max_score',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]