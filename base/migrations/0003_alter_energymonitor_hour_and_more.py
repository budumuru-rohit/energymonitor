# Generated by Django 4.1.5 on 2023-04-01 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0002_alter_energymonitor_day_alter_energymonitor_month_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="energymonitor",
            name="hour",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="energymonitor",
            name="microsecond",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="energymonitor",
            name="minute",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="energymonitor",
            name="second",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
