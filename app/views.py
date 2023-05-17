from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.db.models import Q
from .forms import *
from app.models import Order
from django.db.models import Max


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.success(request, ("Neteisingas vartotojo vardas arba slaptažodis. Bandykite dar kartą."))
            return redirect("user_login")

    else:
        return render(request, "user/login.html", {})
    

def tracking(request):
    if request.method == "POST":
        search = request.POST.get("search")
        try:
            order = Order.objects.get(Q(code=search))
            return render(request, "order/tracking.html", {"search" : search, "order" : order})
        except Order.DoesNotExist:
            messages.error = "Neteisingai įvestas kodas"
            return render(request, "order/tracking.html", {"search": search, "messages": messages.error})
        except ValueError:
            messages.error = "Neteisingai įvestas kodas"
            return render(request, "order/tracking.html", {"search": search, "messages": messages.error})
        
    else:
        return render(request, "order/tracking.html", {})

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, ("Atsijungta sėkmingai"))
    return redirect("user_login")


@login_required
def index(request):
    current_user = request.user
    orders = Order.objects.all().order_by("-created_date")
    return render(request, "main/base.html", {"orders" : orders,
                                              "current_user": current_user})


@login_required
def admission(request, order_id):
    order = Order.objects.get(pk=order_id)
    return render(request, "pdfs/admission.html", {"order" : order})


@login_required
def admission_print(request, order_id):
    order = Order.objects.get(pk=order_id)
    return render(request, "pdfs/admission_print.html", {"order" : order})


@login_required
def add_order(request):
    current_user = request.user
    user = request.user

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            form.save()
            pk = order.id
            order = Order.objects.get(pk=pk)
            order.received_by = user
            last_code = Order.objects.aggregate(Max('code')).get('code__max')
            if last_code is not None:
                order.code = last_code + 1
            else:
                order.code = 22430
            order.save()
            return redirect("order", pk)
    else:
        form = OrderForm()

    return render(request, "order/add_order.html", {"form": form, "current_user": current_user})


@login_required
def add_user(request):
    current_user = request.user
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        print(form.errors)
        if form.is_valid():
            user = form.save()
            pk = user.pk
            return redirect("user", pk)
    else:
        form = CustomUserCreationForm()
    return render(request, 'user/add_user.html', {"form": form,
                                                  "current_user" : current_user})


@login_required
def order(request, order_id):
    current_user = request.user
    order = Order.objects.get(pk=order_id)
    return render(request, "order/order.html", {"order" : order,
                                                "current_user" : current_user})


@login_required
def user(request, user_id):
    current_user = request.user
    user = User.objects.get(pk=user_id)
    return render(request, "user/user.html", {"user": user, "current_user" : current_user, "messages": messages})


@login_required
def update_order(request, order_id):
    order = Order.objects.get(pk=order_id)
    if order.status != "Atiduota klientui":
        order.status = request.POST.get("status")
        if order.status == "Atiduota klientui":
            order.closed_date = date.today()
            order.save()
    else:
        order.status = request.POST.get("status")    

    order.trouble = request.POST.get("trouble")
    order.comment = request.POST.get("comment")
    order.period = request.POST.get("period")
    order.in_type = request.POST.get("in_type")
    order.return_comment = request.POST.get("return_comment")
    order.save()
    return redirect("home")


@login_required
def update_user(request, user_id):
    user = User.objects.get(pk=user_id)
    user.username = request.POST.get("username")
    user.first_name = request.POST.get("first_name")
    user.last_name = request.POST.get("last_name")
    user.email = request.POST.get("email")

    password1 = request.POST.get("password1")
    password2 = request.POST.get("password2")
    if password1 != "" and password2 != "":
        if password1 == password2:
            user.set_password(password1)
            user.save()
            return redirect("user", user_id)

    user.save()    
    return redirect("user", user_id)


@login_required
def update_order_card(request, order_id):
    order = Order.objects.get(pk=order_id)
    if order.status != "Atiduota klientui":
        order.status = request.POST.get("status")
        if order.status == "Atiduota klientui":
            order.closed_date = date.today()
            order.save()
    else:
        order.status = request.POST.get("status")    

    order.trouble = request.POST.get("trouble")
    order.comment = request.POST.get("comment")
    order.period = request.POST.get("period")
    order.in_type = request.POST.get("in_type")
    order.return_comment = request.POST.get("return_comment")
    order.save()
    return redirect("order", order_id)


@login_required
def search_order(request):
    current_user = request.user
    if request.method == "POST":
        search = request.POST["search"]
        orders = Order.objects.filter(
            Q(client_name__contains=search)
            | Q(phone__contains=search)
            | Q(email__contains=search) | Q(code__contains=search) | Q(model__contains=search)
        )

        return render(
            request, "order/search_order.html", {"search" : search, 
                                                 "orders" : orders,
                                                 "current_user" : current_user}
        )
    else:
        orders = Order.objects.all()
        return render(request, "order/search_order.html", {"orders" : orders,
                                                           "current_user" : current_user})
    

@login_required
def search_user(request):
    current_user = request.user
    if request.method == "POST":
        search = request.POST["search"]
        users = User.objects.filter(
            Q(username__contains=search)
            | Q(first_name__contains=search)
            | Q(email__contains=search)
        )

        return render(
            request, "user/search_user.html", {"search" : search, 
                                               "users" : users,
                                               "current_user" : current_user}
        )
    else:
        users = User.objects.all()
        return render(request, "user/search_user.html", {"users" : users,
                                                         "current_user" : current_user})
    
