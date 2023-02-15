class ReverseRuMiddleware:
    def __init__(self, get_response):
        self.count = 1
        self.get_response = get_response

    def __call__(self, request):
        """reverses russian words in each tenth response"""
        alphabet = (
            "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
            "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        )
        response = self.get_response(request)
        content = list(response.content.decode("utf-8"))
        begin = -1
        if not self.count % 10:
            for i in range(len(content) - 1):
                if begin == -1 and content[i] in alphabet:
                    begin = i
                if begin != -1 and content[i + 1] not in alphabet:
                    content[begin : i + 1] = reversed(content[begin : i + 1])
                    begin = -1
            response.content = "".join(content)
        self.count += 1
        return response
