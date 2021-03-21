# Generated by Django 3.1.6 on 2021-03-21 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam_network', '0011_result_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='result',
        ),
        migrations.AddField(
            model_name='result',
            name='answers',
            field=models.ManyToManyField(to='exam_network.Answer'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_network.question'),
        ),
    ]
