# Generated by Django 4.2 on 2023-04-26 10:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "client_name",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("phone", models.CharField(blank=True, max_length=100, null=True)),
                ("email", models.EmailField(blank=True, max_length=100, null=True)),
                (
                    "device_type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Kompiuteris", "Kompiuteris"),
                            ("Telefonas", "Telefonas"),
                        ],
                        max_length=100,
                        null=True,
                    ),
                ),
                ("model", models.CharField(blank=True, max_length=100, null=True)),
                ("comment", models.TextField(blank=True, null=True)),
                (
                    "sn",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Kompiuteris", "Kompiuteris"),
                            ("Telefonas", "Telefonas"),
                        ],
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "test",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Kompiuteris", "Kompiuteris"),
                            ("Telefonas", "Telefonas"),
                        ],
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Garantinis", "Garantinis"),
                            ("Negarantinis", "Negarantinis"),
                        ],
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "priority",
                    models.CharField(
                        blank=True,
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "received_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
