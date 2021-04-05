# Generated by Django 3.0.7 on 2021-04-04 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_network', '0022_auto_20210404_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='id',
            field=models.UUIDField(default='210adfeda97a490d8dc0ecc11478a6d6', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='course',
            name='id',
            field=models.UUIDField(default='cfd28d4245a74fa08eb3541fa43dc4e6', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='exam',
            name='id',
            field=models.UUIDField(default='9e54b60b8b72454581235255c55b1f00', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.UUIDField(default='2e632dff9ba44b80a7551609ad6627ad', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='submission',
            name='id',
            field=models.UUIDField(default='b3fa8e373b9b4fd696599348aef55835', editable=False, primary_key=True, serialize=False),
        ),
    ]