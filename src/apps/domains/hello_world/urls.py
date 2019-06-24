from django.urls import path

from apps.domains.hello_world.views import HelloWorldView

app_name = 'apps.domains.hello_world'
urlpatterns = [
    path('', HelloWorldView.as_view(), name='hello_world_main'),
]
