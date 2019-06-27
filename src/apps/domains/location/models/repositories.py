from datetime import datetime
from typing import List, Optional
from uuid import UUID

from django.contrib.auth.models import User

from apps.domains.location.models.models import GpxCrawlStatus, GpxPoint, GpxShare
from libs.django.db.models.base_repository import BaseRepository


class GpxPointRepository(BaseRepository):
    model_class = GpxPoint

    @classmethod
    def find_by_user_and_term(
            cls, user: User, start_record_time: Optional[datetime], end_record_time: Optional[datetime]
    ) -> List[GpxPoint]:
        qs = cls.model_class.objects.filter(user=user).order_by('record_time')

        if start_record_time:
            qs = qs.filter(record_time__gte=start_record_time)

        if end_record_time:
            qs = qs.filter(record_time__lte=end_record_time)

        return qs


class GpxCrawlStatusRepository(BaseRepository):
    model_class = GpxCrawlStatus

    @classmethod
    def find_avail_all(cls) -> List[GpxCrawlStatus]:
        return cls.model_class.objects.filter(is_active=True)


class GpxShareRepository(BaseRepository):
    model_class = GpxShare

    @classmethod
    def get_by_uuid(cls, uuid: UUID) -> GpxShare:
        return cls.model_class.objects.get(share_uuid=uuid)
