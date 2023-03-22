from datetime import timedelta

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.http.response import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from myserver.settings import DEFAULT_FROM_EMAIL

from users.forms import MyLoginForm, MyUserCreationForm, ProfileForm, UserForm
from users.models import Profile


def signup(request):
    form = MyUserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.save()
        Profile.objects.create(user=user)
        send_mail(
            "wtf",
            f"http://127.0.0.1/auth/activate/{form.cleaned_data['username']}/",
            DEFAULT_FROM_EMAIL,
            [form.cleaned_data["username"]],
        )
        return redirect("homepage:home")
    return render(request, "users/signup.html", {"form": form})


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    authentification_form = MyLoginForm

    # catch superusers and manually created others
    def form_valid(self, form):
        usr = User.objects.get(username=self.request.POST["username"])
        _, _ = Profile.objects.get_or_create(user=usr)
        return super().form_valid(form)


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
        "active_users": User.objects.filter(is_active=True).only("username"),
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
