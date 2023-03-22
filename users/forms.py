from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import (
    DateField,
    DateInput,
    IntegerField,
    ModelForm,
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


class MyLoginForm(AuthenticationForm, BootstrapClassesMixin):
    pass


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
