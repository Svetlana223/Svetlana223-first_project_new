# Generated by Django 5.0.2 on 2024-02-21 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0002_alter_articlemodel_public_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='public_flag',
            field=models.BooleanField(default=False),
        ),
    ]