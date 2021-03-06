from django.urls import path

from apps.domains.location.views import GpxShareFileView, GpxShareView, LocationIndexView, GpxView, GpxFileView

app_name = 'apps.domains.location'
urlpatterns = [
    path('', LocationIndexView.as_view(), name='index'),

    path('gpx/by-date/', GpxView.as_view(), name='gpx'),
    path('gpx/by-date/file', GpxFileView.as_view(), name='gpx_file'),

    path('gpx/share/<uuid:share_uuid>/', GpxShareView.as_view(), name='gpx_share'),
    path('gpx/share/<uuid:share_uuid>/file', GpxShareFileView.as_view(), name='gpx_share_file'),
]
