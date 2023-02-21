import django.core.exceptions
from django.utils.deconstruct import deconstructible


@deconstructible
class GreatValidator:
    def __init__(self, *args):
        self.args = args

    def __call__(self, value):
        exists = False
        for arg in self.args:
            if arg in value.split():
                exists = True
        if not exists:
            raise django.core.exceptions.ValidationError(
                f"Поле должно сдержать одно из: {' '.join(self.args)}"
            )
