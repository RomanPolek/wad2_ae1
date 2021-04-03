# Generated by Django 3.0.7 on 2021-04-03 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_network', '0019_auto_20210403_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='id',
            field=models.UUIDField(default='a07f0ff449bf47f3a92c5cf67e4591e3', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='course',
            name='id',
            field=models.UUIDField(default='24aceceed0c04d3f967a1bac4a595d8f', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='exam',
            name='id',
            field=models.UUIDField(default='e39b37a40ff34adc8f001f90e7e88b71', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.UUIDField(default='e7db4a05a1324cd5aa1b16c17c4318fd', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.UUIDField(default='a38fc5a1049c468e8cde79170d14729f', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='submission',
            name='id',
            field=models.UUIDField(default='4a131286761641018f0657c64334b978', editable=False, primary_key=True, serialize=False),
        ),
    ]