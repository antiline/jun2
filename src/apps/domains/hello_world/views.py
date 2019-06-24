from django.shortcuts import render
from django.views import View


class HelloWorldView(View):
    def get(self, request):
        return render(request, 'hello_world/index.html', {})
