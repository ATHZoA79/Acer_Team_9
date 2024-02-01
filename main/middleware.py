from django.shortcuts import redirect
from django.http import HttpRequest, HttpResponseRedirect
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
        if not request.user.is_authenticated:
            return HttpResponseRedirect("account_login")
        else:
            response = self.get_response(request)
            return response
