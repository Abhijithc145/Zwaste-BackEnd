# Generated by Django 4.0.4 on 2022-06-27 06:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admins', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todaywork',
            name='Driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Drivername', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='todaywork',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Username', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='purchases',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admins.products'),
        ),
        migrations.AddField(
            model_name='purchases',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='driverregistration',
            name='Drivename',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
