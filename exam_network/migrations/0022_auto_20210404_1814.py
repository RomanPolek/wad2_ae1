# Generated by Django 3.0.7 on 2021-04-04 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_network', '0021_auto_20210404_1616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='choice_5',
        ),
        migrations.AddField(
            model_name='question',
            name='choice_0',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='answer',
            name='id',
            field=models.UUIDField(default='5699aab5b3884443b46700a6f41f57c1', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='course',
            name='id',
            field=models.UUIDField(default='375941fea7a943808c6e7c9a09049748', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='exam',
            name='id',
            field=models.UUIDField(default='f1f1c812a3bf4bf4a21771400fe7d435', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.UUIDField(default='37a2530905b94f8a9fda7f348cc782d0', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='submission',
            name='id',
            field=models.UUIDField(default='3bc07981a87b468cb4e8f1830a95d142', editable=False, primary_key=True, serialize=False),
        ),
    ]