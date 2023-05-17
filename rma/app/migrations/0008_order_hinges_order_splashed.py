# Generated by Django 4.1.6 on 2023-04-29 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0007_order_scratched_screen_alter_order_charger_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="hinges",
            field=models.CharField(
                choices=[("Taip", "Taip"), ("Ne", "Ne")], default="Ne", max_length=4
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="splashed",
            field=models.CharField(
                choices=[("Taip", "Taip"), ("Ne", "Ne")], default="Ne", max_length=4
            ),
        ),
    ]