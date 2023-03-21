from datetime import timedelta

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http.response import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from myserver.settings import DEFAULT_FROM_EMAIL

from users.forms import ProfileForm, UserForm
from users.models import Profile


def signup(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.save()
        send_mail(
            "wtf",
            f"http://127.0.0.1/auth/activate/{form.cleaned_data['username']}/",
            DEFAULT_FROM_EMAIL,
            [form.cleaned_data["username"]],
        )
        return redirect("homepage:home")
    return render(request, "users/signup.html", {"form": form})


@login_required
def profile_view(request):
    user = UserForm(request.POST or None, instance=request.user)
    user_detail = Profile.objects.get(user=request.user.id)
    profile = ProfileForm(
        request.POST or None,
        request.FILES,
        instance=user_detail,
    )

    if user.is_valid() and profile.is_valid():
        user.save()
        profile.save()
        return redirect("homepage:home")

    context = {
        "user_form": user,
        "profile_form": profile,
    }
    return render(request, "users/profile.html", context)


def get_user_list(request):
    context = {
        "active_users": User.objects.filter(is_active=True).only("username"),
    }
    return render(request, "users/user_list.html", context)


def get_user_detail(request, id):
    context = {
        "user_detail": User.objects.select_related("profile").get(pk=id)
    }
    return render(request, "users/user_detail.html", context)


def activation_view(request, username):
    usr = get_object_or_404(User, username=username)
    if (
        usr.date_joined + timedelta(hours=12) >= timezone.now()
        and not usr.is_active
    ):
        usr.is_active = True
        usr.save()
        Profile.objects.create(user=usr)
        return redirect("users:login")
    else:
        raise Http404("token expired")
