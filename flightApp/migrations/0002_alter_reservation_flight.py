# Generated by Django 4.0.5 on 2022-07-22 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flightApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='flight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flightApp.flight'),
        ),
    ]
