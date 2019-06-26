from django.urls import path

from apps.domains.home.views import HomeIndexView

app_name = 'apps.domains.home'
urlpatterns = [
    path('', HomeIndexView.as_view(), name='home_index'),
]
