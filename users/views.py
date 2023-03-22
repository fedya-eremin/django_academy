from datetime import timedelta

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.db import IntegrityError
from django.http.response import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from myserver.settings import DEFAULT_FROM_EMAIL

from users.forms import MyLoginForm, MyUserCreationForm, ProfileForm, UserForm
from users.models import Profile, ProxyUser


def signup(request):
    form = MyUserCreationForm(request.POST or None)
    if form.is_valid():
        try:
            user = form.save(commit=False)
            user.email = user.username
            user.save()
            Profile.objects.create(user=user)

        except IntegrityError:
            form.add_error(None, ValidationError(message="Уже есть такой"))
            return render(request, "users/signup.html", {"form": form})

        send_mail(
            "wtf",
            f"http://127.0.0.1/auth/activate/{form.cleaned_data['username']}/",
            DEFAULT_FROM_EMAIL,
            [form.cleaned_data["username"]],
        )
        return redirect("homepage:home")
    return render(request, "users/signup.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = MyLoginForm(data=request.POST)
        print(form.is_valid())
        print(request.POST)
        if form.is_valid():
            print(123)
            data = form.cleaned_data
            usr = authenticate(
                username=data["username"], password=data["password"]
            ) or ProxyUser.objects.get(email=data["username"])
            _, _ = Profile.objects.get_or_create(user=usr)
            if usr is not None and usr.is_active:
                login(request, usr)
                return redirect("users:profile")
    else:
        form = MyLoginForm()
    return render(request, "users/login.html", {"form": form})


@login_required
def profile_view(request):
    user = UserForm(request.POST or None, instance=request.user)
    profile = ProfileForm(
        data=request.POST or None,
        files=request.FILES or None,
        instance=request.user.profile,
    )

    if user.is_valid() and profile.is_valid():
        if "Coffee" in request.POST:
            request.user.profile.coffee_count += 1
            request.user.save()
        user.save()
        profile.save()
        return redirect("users:profile")

    context = {
        "user_form": user,
        "profile_form": profile,
    }
    return render(request, "users/profile.html", context)


def get_user_list(request):
    context = {
        "active_users": ProxyUser.objects.only("username"),
    }
    return render(request, "users/user_list.html", context)


def get_user_detail(request, id):
    context = {"user_detail": get_object_or_404(User, pk=id)}
    return render(request, "users/user_detail.html", context)


def activation_view(request, username):
    usr = get_object_or_404(User, username=username)
    if (
        usr.date_joined + timedelta(hours=12) >= timezone.now()
        and not usr.is_active
    ):
        usr.is_active = True
        usr.save()
        return redirect("users:login")
    else:
        raise Http404("token expired")
