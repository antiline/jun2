from django.forms import Form
from django_filters.fields import IsoDateTimeField


class GpxForm(Form):
    start_time = IsoDateTimeField(label='시작 시간')
    end_time = IsoDateTimeField(label='끝 시간')


class GpxFileForm(Form):
    start_time = IsoDateTimeField(label='시작 시간')
    end_time = IsoDateTimeField(label='끝 시간')
