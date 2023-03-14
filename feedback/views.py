from django.core.mail import send_mail
from django.shortcuts import redirect, render

from feedback.forms import FeedbackForm
from feedback.models import (
    ComplainingUserModel,
    FeedbackAttachments,
    FeedbackModel,
)

from myserver.settings import DEFAULT_FROM_EMAIL


def feedback(request):
    form = FeedbackForm(request.POST or None, request.FILES)
    if form.is_valid():
        text = form.cleaned_data.get("text")
        address = form.cleaned_data.get("email")
        name = form.cleaned_data.get("name")
        files = request.FILES.getlist("file_field")
        print(request.FILES)
        author = ComplainingUserModel.objects.create(email=address, name=name)
        feedback = FeedbackModel.objects.create(text=text, author=author)
        for file in files:
            FeedbackAttachments.objects.create(file=file, feedback=feedback)
        send_mail(
            "Feedback",
            text,
            DEFAULT_FROM_EMAIL,
            [address],
            fail_silently=False,
        )
        return redirect("feedback:feedback_success")
    # else:
    #     raise django.forms.ValidationError("Введите корректный email!")
    context = {
        "form": form,
    }
    return render(request, "feedback/feedback.html", context)


def feedback_success(request):
    return render(request, "feedback/feedback_success.html")
