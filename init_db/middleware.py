from django.shortcuts import redirect
from django.http import HttpRequest
import logging

logger = logging.getLogger(__name__)


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.excluded_paths = [
            "/",
        ]

    def __call__(self, request: HttpRequest):
        logger.debug(f"Request path: {request.path}")
        if request.user.is_staff and request.path.startswith("/init"):
            response = self.get_response(request)
        else:
            return redirect("account_login")
        return response
