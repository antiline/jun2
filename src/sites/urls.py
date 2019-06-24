from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from apps.domains.hello_world import urls as hello_world_urls

urlpatterns = [
    path('internal-admin/', admin.site.urls),
    path('hello-world/', include(hello_world_urls, namespace='hello_world')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
