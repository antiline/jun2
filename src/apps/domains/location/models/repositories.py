from typing import List

from django.contrib.auth.models import User

from apps.domains.location.models.models import GpxPoint
from libs.django.db.models.base_repository import BaseRepository


class GpxPointRepository(BaseRepository):
    model_class = GpxPoint

    @classmethod
    def find_by_user(cls, user: User) -> List[GpxPoint]:
        return cls.model_class.objects.filter(user=user)
