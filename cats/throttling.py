from rest_framework import throttling
import datetime

class LowRequestRateThrottle(throttling.BaseThrottle):
    def allow_request(self, request, view):
        now = datetime.datetime.now().hour
        if now >= 22 and now <= 0:
            return False
        return True