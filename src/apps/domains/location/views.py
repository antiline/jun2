from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from apps.domains.location.services.gpx_share_service import GpxShareService


class LocationIndexView(View):
    def get(self, request):
        return render(request, 'location/index.html', {})


class GpxShareView(View):
    def get(self, request, share_uuid):
        return render(request, 'location/gpx_share.html', {'share_uuid': share_uuid})


class GpxShareFileView(View):
    def get(self, request, share_uuid):
        gpx = GpxShareService.get_gpx_by_uuid(share_uuid)
        return HttpResponse(gpx.to_xml())
