# Generated by Django 4.0.4 on 2022-06-29 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userregister',
            name='Pic_code',
        ),
        migrations.AddField(
            model_name='userregister',
            name='District',
            field=models.CharField(max_length=30, null=True),
        ),
    ]