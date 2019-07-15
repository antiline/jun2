from django.shortcuts import render
from django.views import View


class HomeIndexView(View):
    @staticmethod
    def get(request):
        return render(request, 'home/index.html', {})
