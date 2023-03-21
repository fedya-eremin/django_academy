from django.contrib.auth.models import User
from django.forms import DateField, DateInput, IntegerField, ModelForm

from users.models import Profile


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ("username", "email")

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for visible_field in self.visible_fields():
            visible_field.field.widget.attrs[
                "class"
            ] = "form-control form-control-lg form-group-item"


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ("birthday", "image", "coffee_count")

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for visible_field in self.visible_fields():
            visible_field.field.widget.attrs[
                "class"
            ] = "form-control form-control-lg form-group-item"

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
        required=False,
    )
