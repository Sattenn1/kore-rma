from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from .models import *


class OrderForm(ModelForm):
    DEVICE_CHOICES = [
        ("Kompiuteris", "Kompiuteris"),
        ("Vaizdo Plokštė", "Vaizdo Plokštė"),
        ("Motininė plokštė", "Motininė plokštė"),
        ("Įkroviklis", "Įkroviklis"),
        ("GPS", "GPS"),
        ("Kita", "Kita")
    ]

    CHOICES_Y_N = [("Taip", "Taip"), ("Ne", "Ne")]

    device_type = forms.ChoiceField(choices=DEVICE_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    priority = forms.ChoiceField(choices=CHOICES_Y_N, widget=forms.Select(attrs={'class': 'form-select'}))
    type = forms.ChoiceField(choices=CHOICES_Y_N, widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = Order
        fields = ("client_name", "phone", "email", "device_type", "model",
                  "comment", "trouble", "type", "priority", "charger", 
                  "keyboard", "scratched", "cracked", "scratched_screen",
                  "hinges", "splashed", "s_n")

        widgets = {
            "client_name": forms.TextInput(attrs={'class': 'form-control'}),
            "phone": forms.TextInput(attrs={'class': 'form-control'}),
            "email": forms.EmailInput(attrs={'class': 'form-control'}),
            "model": forms.TextInput(attrs={'class': 'form-control'}),
            "s_n": forms.TextInput(attrs={'class': 'form-control'}),
            "trouble": forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}),
            "comment": forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}),
            "priority": forms.Select(attrs={'class': 'form-select'}),
            "scratched": forms.RadioSelect(choices=[('Taip', 'Taip'), ('Ne', 'Ne')], attrs={'class': 'form-check-input form-check-inline'}),
            "scratched_screen": forms.RadioSelect(choices=[('Taip', 'Taip'), ('Ne', 'Ne')], attrs={'class': 'form-check-input form-check-inline'}),
            "cracked": forms.RadioSelect(choices=[('Taip', 'Taip'), ('Ne', 'Ne')], attrs={'class': 'form-check-input form-check-inline'}),
            "charger": forms.RadioSelect(choices=[('Taip', 'Taip'), ('Ne', 'Ne')], attrs={'class': 'form-check-input form-check-inline'}),
            "keyboard": forms.RadioSelect(choices=[('Taip', 'Taip'), ('Ne', 'Ne')], attrs={'class': 'form-check-input form-check-inline'}),
            "hinges": forms.RadioSelect(choices=[('Taip', 'Taip'), ('Ne', 'Ne')], attrs={'class': 'form-check-input form-check-inline'}),
            "splashed": forms.RadioSelect(choices=[('Taip', 'Taip'), ('Ne', 'Ne')], attrs={'class': 'form-check-input form-check-inline'}),
        }

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['device_type'].initial = 'Kompiuteris'
        self.fields['priority'].initial = 'Ne'
        self.fields['type'].initial = 'Ne'
        self.fields["phone"].initial = "+370"


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        initial=[Group.objects.get(name='Darbuotojai')]
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'groups']
        widgets = {
            "username": forms.TextInput(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            self.save_m2m()
        return user
