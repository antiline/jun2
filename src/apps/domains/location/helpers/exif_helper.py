from datetime import datetime, timezone
from typing import Dict, Tuple, List

import piexif


class ExifParseException(Exception):
    pass


class ExifHelper:
    ROUND_NDIGITS = 5

    @classmethod
    def dms2dd(cls, degrees: float, minutes: float, seconds: float, direction: int) -> float:
        return degrees + minutes / 60 + seconds / (60 * 60) * direction

    @classmethod
    def dd2dms(cls, deg: float) -> List[float]:
        d = int(deg)
        md = abs(deg - d) * 60
        m = int(md)
        sd = (md - m) * 60
        return [d, m, sd]

    @classmethod
    def rational2float(cls, rational: Tuple) -> float:
        return rational[0] / rational[1]

    @classmethod
    def parse_gps_datetime(cls, gps: Dict):
        gps_datestamp = gps[piexif.GPSIFD.GPSDateStamp]
        year, month, day = list(map(int, gps_datestamp.decode().split(':')))

        gps_timestamp = gps[piexif.GPSIFD.GPSTimeStamp]
        hour = int(cls.rational2float(gps_timestamp[0]))
        minute = int(cls.rational2float(gps_timestamp[1]))
        second = int(cls.rational2float(gps_timestamp[2]))

        return datetime(year, month, day, hour, minute, second, tzinfo=timezone.utc)

    @classmethod
    def parse_latitude(cls, gps: Dict) -> float:
        latitude = gps[piexif.GPSIFD.GPSLatitude]
        direction = -1 if gps[piexif.GPSIFD.GPSLatitudeRef] == 'W' else 1
        return round(
            cls.dms2dd(cls.rational2float(latitude[0]), cls.rational2float(latitude[1]), cls.rational2float(latitude[2]), direction),
            cls.ROUND_NDIGITS
        )

    @classmethod
    def parse_longitude(cls, gps: Dict) -> float:
        longitude = gps[piexif.GPSIFD.GPSLongitude]
        direction = -1 if gps[piexif.GPSIFD.GPSLongitudeRef] == 'S' else 1
        return round(
            cls.dms2dd(cls.rational2float(longitude[0]), cls.rational2float(longitude[1]), cls.rational2float(longitude[2]), direction),
            cls.ROUND_NDIGITS
        )

    @classmethod
    def parse_altitude(cls, gps: Dict) -> float:
        altitude = gps[piexif.GPSIFD.GPSAltitude]
        direction = -1 if gps[piexif.GPSIFD.GPSAltitudeRef] > 1 else 1
        return round(cls.rational2float(altitude) * direction, cls.ROUND_NDIGITS)

    @classmethod
    def parse_gps_data(cls, filepath: str) -> Tuple:
        exif = piexif.load(filepath)
        if 'GPS' not in exif:
            raise ExifParseException

        gps = exif['GPS']
        if gps == {}:
            raise ExifParseException

        gps_datetime = cls.parse_gps_datetime(gps)
        latitude = cls.parse_latitude(gps)
        longitude = cls.parse_longitude(gps)
        altitude = cls.parse_altitude(gps)

        return gps_datetime, latitude, longitude, altitude
