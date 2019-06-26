from django.urls import path

from apps.domains.location.views import GpxShareFileView, GpxShareView, LocationIndexView

app_name = 'apps.domains.location'
urlpatterns = [
    path('', LocationIndexView.as_view(), name='index'),
    path('gpx/share/<uuid:share_uuid>/', GpxShareView.as_view(), name='gpx_share'),
    path('gpx/share/<uuid:share_uuid>/file', GpxShareFileView.as_view(), name='gpx_share_file'),
]
