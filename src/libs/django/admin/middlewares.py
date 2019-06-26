from admin_ip_restrictor.middleware import AdminIPRestrictorMiddleware as BaseAdminIPRestrictorMiddleware
from ipware import get_client_ip


class AdminIPRestrictorMiddleware(BaseAdminIPRestrictorMiddleware):
    def get_ip(self, request):
        client_ip, _ = get_client_ip(request)
        return client_ip
