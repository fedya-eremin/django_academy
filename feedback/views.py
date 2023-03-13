from django.core.mail import send_mail
from django.shortcuts import redirect, render

from feedback.forms import FeedbackForm
from feedback.models import FeedbackModel

from myserver.settings import DEFAULT_FROM_EMAIL


def feedback(request):
    form = FeedbackForm(request.POST or None)
    if form.is_valid():
        text = form.cleaned_data.get("text")
        address = form.cleaned_data.get("email")
        FeedbackModel.objects.create(text=text, email=address)
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
