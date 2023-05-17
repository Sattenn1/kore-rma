# Generated by Django 4.1.6 on 2023-05-08 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0016_alter_order_code"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="in_type",
            field=models.CharField(
                blank=True,
                choices=[("Taip", "Taip"), ("Ne", "Ne")],
                max_length=100,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="period",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="return_comment",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Užregistruotas gedimas", "Užregistruotas gedimas"),
                    ("Taisoma", "Taisoma"),
                    ("Laukiama dalių", "Laukiama dalių"),
                    ("Pataisyta", "Pataisyta"),
                    ("Atiduota klientui", "Atiduota klientui"),
                ],
                default="Užregistruotas gedimas",
                max_length=100,
                null=True,
            ),
        ),
    ]
