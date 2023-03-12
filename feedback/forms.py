import django.forms


class FeedbackForm(django.forms.Form):
    text = django.forms.CharField(
        label="Текст",
        help_text="Введите текст фидбека",
        widget=django.forms.Textarea(
            attrs={"class": "form-control form-control-lg"}
        ),
    )
    email = django.forms.EmailField(
        label="Почта",
        help_text="Введите почтовый адрес",
        widget=django.forms.TextInput(
            attrs={"class": "form-control form-control-lg"}
        ),
    )
