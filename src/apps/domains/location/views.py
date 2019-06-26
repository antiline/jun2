from django.shortcuts import render
from django.views import View


class LocationIndexView(View):
    def get(self, request):
        return render(request, 'location/index.html', {})
