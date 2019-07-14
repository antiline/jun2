from datetime import datetime

import gpxpy
import gpxpy.gpx
from django.contrib.auth.models import User

from apps.domains.location.models.repositories import GpxPointRepository


class GpxService:
    @classmethod
    def get_gpx(cls, user: User, start_record_time: datetime, end_record_time: datetime, reduce=True) -> gpxpy.gpx.GPX:
        gpx = gpxpy.gpx.GPX()

        # Create first track in our GPX:
        gpx_track = gpxpy.gpx.GPXTrack()
        gpx.tracks.append(gpx_track)

        # Create first segment in our GPX track:
        gpx_segment = gpxpy.gpx.GPXTrackSegment()
        gpx_track.segments.append(gpx_segment)

        # Create points:
        points = GpxPointRepository.find_by_user_and_term(user, start_record_time, end_record_time)
        for point in points:
            gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(point.latitude, point.longitude, point.elevation, point.record_time))

        if reduce:
            gpx.reduce_points(min_distance=1)
            gpx.simplify()

        return gpx
