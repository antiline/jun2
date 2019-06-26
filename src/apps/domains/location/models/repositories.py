from apps.domains.location.models.models import Gpx
from libs.django.db.models.base_repository import BaseRepository


class GpxRepository(BaseRepository):
    model_class = Gpx
