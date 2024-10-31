from datetime import timedelta
from django.contrib.auth import logout
from django.utils import timezone


class AutoLogoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.inactivity_threshold = timedelta(minutes=1)

    def __call__(self, request):
        if request.user.is_authenticated:
            now = timezone.now()

            last_active = request.user.last_active_datetime

            if last_active and now - last_active > self.inactivity_threshold:
                logout(request)
            else:
                # it can be optimized, for example with uniform distribution.
                request.user.last_active_datetime = now
                request.user.save(update_fields=['last_active_datetime'])

        response = self.get_response(request)
        return response
