# Generated by Django 2.2.12 on 2020-06-04 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mumbletemps', '0002_tempuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tempuser',
            name='user_name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]