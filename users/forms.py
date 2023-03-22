from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import (
    CharField,
    DateField,
    DateInput,
    Form,
    IntegerField,
    ModelForm,
    PasswordInput,
    TextInput,
)

from users.models import Profile


class BootstrapClassesMixin(ModelForm):
    """
    applies bootstrap form
    """

    def __init__(self, *args, **kwargs):
        super(BootstrapClassesMixin, self).__init__(*args, **kwargs)
        for visible_field in self.visible_fields():
            visible_field.field.widget.attrs[
                "class"
            ] = "form-control form-control-lg form-group-item"


class MyUserCreationForm(UserCreationForm, BootstrapClassesMixin):
    pass


class MyLoginForm(Form):
    username = CharField(
        label="Пользователь",
        max_length=150,
        widget=TextInput(attrs={"autofocus": True}),
    )
    password = CharField(
        label="Пароль",
        strip=False,
        widget=PasswordInput(attrs={"autocomplete": "current-password"}),
    )


class UserForm(BootstrapClassesMixin):
    class Meta:
        model = User
        fields = ("username", "email")


class ProfileForm(BootstrapClassesMixin):
    class Meta:
        model = Profile
        fields = ("birthday", "image", "coffee_count")

    birthday = DateField(
        label="Дата рождения",
        required=False,
        widget=DateInput(
            attrs={
                "type": "text",
                "placeholder": "dd.mm.yyyy",
            }
        ),
    )

    coffee_count = IntegerField(
        label="Выпито кофе",
        widget=TextInput(
            attrs={
                "readonly": True,
            }
        ),
    )
