from uuid import UUID

import gpxpy.gpx
from django.core.exceptions import ObjectDoesNotExist

from apps.domains.location.models.repositories import GpxShareRepository
from apps.domains.location.services.gpx_service import GpxService


class GpxShareService:
    @classmethod
    def get_gpx_by_uuid(cls, share_uuid: UUID) -> gpxpy.gpx.GPX:
        gpx_share = GpxShareRepository.get_by_uuid(share_uuid)
        if not gpx_share.is_active:
            raise ObjectDoesNotExist

        return GpxService.get_gpx(gpx_share.user, gpx_share.start_record_time, gpx_share.end_record_time)
