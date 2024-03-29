import django.forms


class FeedbackForm(django.forms.Form):
    text = django.forms.CharField(
        label="Текст",
        help_text="Введите текст фидбека",
        widget=django.forms.Textarea(
            attrs={"class": "form-control form-control-lg form-group-item"}
        ),
    )
    name = django.forms.CharField(
        label="Твоё имя",
        help_text="Введите имя",
        widget=django.forms.TextInput(
            attrs={"class": "form-control form-control-lg form-group-item"}
        ),
    )

    email = django.forms.EmailField(
        label="Почта",
        help_text="Введите почтовый адрес",
        widget=django.forms.TextInput(
            attrs={"class": "form-control form-control-lg"}
        ),
    )
    file_field = django.forms.FileField(
        label="Файлы",
        help_text="Прикрепит файлы, которые могут нам помочь",
        widget=django.forms.ClearableFileInput(
            attrs={
                "multiple": True,
                "class": "form-control form-control-lg form-group-item",
            }
        ),
        required=False,
    )
