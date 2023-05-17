from django.contrib import admin
from app import views
from django.urls import path


urlpatterns = [
    path("", views.index, name="home"),
    path("sekimas", views.tracking, name="tracking"),
    path("prisijungti", views.user_login, name="user_login"),
    path("atsijungti", views.user_logout, name="user_logout"),
    path("prideti_uzsakyma", views.add_order, name="add_order"),
    path("koreguoti_uzsakyma/<order_id>", views.update_order, name="update_order"),
    path("koreguoti_uzsakymo_kortele/<order_id>", views.update_order_card, name="update_order_card"),
    path("uzsakymas/<order_id>", views.order, name="order"),
    path("prideti_naudotoja", views.add_user, name="add_user"),
    path("naudotojas/<user_id>", views.user, name="user"),
    path("koreguoti_naudotoja/<user_id>", views.update_user, name="update_user"),
    path("ieskoti_uzsakymo", views.search_order, name="search_order"),
    path("ieskoti_naudotojo", views.search_user, name="search_user"),
    path("pazyma/<order_id>", views.admission_print, name="admission_print"),
    path("pazyma_perziureti/<order_id>", views.admission, name="admission"),

]