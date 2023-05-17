from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Order(models.Model):
    devices = (
        ("Kompiuteris", "Kompiuteris"),
        ("Vaizdo Plokštė", "Vaizdo Plokštė"),
        ("Motininė plokštė", "Motininė plokštė"),
        ("Įkroviklis", "Įkroviklis"),
        ("GPS", "GPS"),
        ("Kita", "Kita")
    )
    
    types = (
        ("Taip", "Taip"),
        ("Ne", "Ne")
    )
    
    in_type = (
        ("Taip", "Taip"),
        ("Ne", "Ne")
    )
    
    priority = (
        ("Taip", "Taip"),
        ("Ne", "Ne")
    )
    
    status = (
        ("Užregistruotas gedimas", "Užregistruotas gedimas"),
        ("Taisoma", "Taisoma"),
        ("Laukiama dalių", "Laukiama dalių"),
        ("Pataisyta", "Pataisyta"),
        ("Atiduota klientui", "Atiduota klientui")
    )

    id = models.BigAutoField(primary_key=True)
    client_name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)

    device_type = models.CharField(max_length=100, choices=devices, null=True, blank=True)
    model = models.CharField(max_length=100, null=True, blank=True)
    s_n = models.CharField(max_length=100, null=True, blank=True)
    trouble = models.CharField(max_length=500, null=True, blank=True)
    comment = models.CharField(max_length=500, null=True, blank=True)

    received_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, choices=type, null=True, blank=True)
    priority = models.CharField(max_length=100, choices=priority, null=True, blank=True)
    status = models.CharField(max_length=100, default="Užregistruotas gedimas", choices=status, null=True, blank=True)

    scratched = models.CharField(max_length=4, default="Ne", null=True, blank=True)
    scratched_screen = models.CharField(max_length=4, default="Ne", null=True, blank=True)
    cracked = models.CharField(max_length=4, default="Ne", null=True, blank=True)
    charger = models.CharField(max_length=4, default="Ne", null=True, blank=True)
    keyboard = models.CharField(max_length=4, default="Ne", null=True, blank=True)
    hinges = models.CharField(max_length=4, default="Ne", null=True, blank=True)
    splashed = models.CharField(max_length=4, default="Ne", null=True, blank=True)

    created_date = models.DateField(default=date.today, null=True, blank=True)
    closed_date = models.DateField(null=True, blank=True)
    in_type = models.CharField(max_length=100, default="Ne", choices=in_type, null=True, blank=True)
    period = models.IntegerField(null=True, blank=True, default="0")
    return_comment = models.CharField(max_length=500, null=True, blank=True)

    code = models.IntegerField(unique=True, null=True, blank=True)

    class Meta:
        db_table = 'app_order'
    
