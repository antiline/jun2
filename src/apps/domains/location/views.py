from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views import View

from apps.domains.location.forms import GpxFileForm, GpxForm
from apps.domains.location.services.gpx_service import GpxService
from apps.domains.location.services.gpx_share_service import GpxShareService
from libs.django.utils.url import reverse_with_query


class LocationIndexView(View):
    @staticmethod
    @login_required
    def get(request):
        return render(request, 'location/index.html', {})


class GpxView(View):
    @staticmethod
    @login_required
    def get(request):
        form = GpxForm(request.GET)
        if not form.is_valid():
            return HttpResponseBadRequest()

        gpx_file_url = reverse_with_query('location:gpx_file', query_kwargs={
            'start_time': form.cleaned_data['start_time'],
            'end_time': form.cleaned_data['end_time']
        })
        return render(request, 'location/gpx.html', {'gpx_file_url': gpx_file_url})


class GpxFileView(View):
    @staticmethod
    @login_required
    def get(request):
        form = GpxFileForm(request.GET)
        if not form.is_valid():
            return HttpResponseBadRequest()

        start_time, end_time = form.cleaned_data['start_time'], form.cleaned_data['end_time']
        gpx = GpxService.get_gpx(request.user, start_time, end_time)

        response = HttpResponse(gpx.to_xml(), content_type='text/plain')
        response['Content-Disposition'] = f'attachment; filename="{start_time}-{end_time}.gpx"'
        return response


class GpxShareView(View):
    @staticmethod
    def get(request, share_uuid):
        gpx_file_url = reverse_with_query('location:gpx_share_file', kwargs={'share_uuid': share_uuid})
        return render(request, 'location/gpx.html', {'gpx_file_url': gpx_file_url})


class GpxShareFileView(View):
    @staticmethod
    def get(request, share_uuid):
        gpx = GpxShareService.get_gpx_by_uuid(share_uuid)

        response = HttpResponse(gpx.to_xml(), content_type='text/plain')
        response['Content-Disposition'] = f'attachment; filename="{share_uuid}.gpx"'
        return response
