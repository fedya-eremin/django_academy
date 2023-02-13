class UIntConverter:
    regex = r"\d*"

    def to_python(self, value):
        return str(value)

    def to_url(self, value):
        return "%d" % value
