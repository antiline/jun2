from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

from apps.domains.home import urls as home_urls
from apps.domains.location import urls as location_urls

urlpatterns = [
    path('', RedirectView.as_view(url='/home/', permanent=False), name='index'),
    path('internal-admin/', admin.site.urls),
    path('home/', include(home_urls, namespace='home')),
    path('location/', include(location_urls, namespace='location')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
