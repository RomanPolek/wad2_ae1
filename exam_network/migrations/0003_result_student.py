# Generated by Django 3.1.6 on 2021-03-19 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam_network', '0002_user_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='student',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='exam_network.user'),
            preserve_default=False,
        ),
    ]
