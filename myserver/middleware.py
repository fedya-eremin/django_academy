import re


class ReverseRuMiddleware:
    def __init__(self, get_response):
        self.count = 1
        self.get_response = get_response

    def __call__(self, request):
        """reverses russian words in each tenth response"""
        response = self.get_response(request)
        try:
            content = list(response.content.decode("utf-8"))
        except AttributeError:
            return response
        begin = -1
        if not self.count % 10:
            for i in range(len(content) - 1):
                if (
                    begin == -1
                    and re.search(r"[а-яА-ЯёЁ]", content[i]) is not None
                ):
                    begin = i
                if (
                    begin != -1
                    and re.search(r"[а-яА-ЯёЁ]", content[i + 1]) is None
                ):
                    content[begin : i + 1] = reversed(content[begin : i + 1])
                    begin = -1
            response.content = "".join(content)
        self.count += 1
        return response
