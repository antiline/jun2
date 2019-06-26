from django.urls import path

from apps.domains.location.views import LocationIndexView

app_name = 'apps.domains.location'
urlpatterns = [
    path('', LocationIndexView.as_view(), name='location_index'),
]
