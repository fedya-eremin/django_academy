import re

import django.core.exceptions
from django.utils.deconstruct import deconstructible


@deconstructible
class GreatValidator:
    def __init__(self, *args):
        self.args = args

    def __call__(self, value):
        """
        regexp defines that word can begin with capital or lowercase, then only
        lowercase letters and end with any amount of literary punctuation
        marks. words are divided by spaces
        """
        exists = False
        for arg in self.args:
            reg = re.compile(
                f"^({arg[0].upper()}|{arg[0].lower()}){arg[1:]}[!?.,]*$"
            )
            for elem in value.plain.split():
                if re.fullmatch(reg, elem):
                    exists = True
        if not exists:
            raise django.core.exceptions.ValidationError(
                f"Поле должно сдержать одно из: {' '.join(self.args)}"
            )
