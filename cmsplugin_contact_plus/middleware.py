from django.http import HttpResponsePermanentRedirect
from .exceptions import MakeRedirectException


class ContactPlusMiddleware:

    def process_exception(self, request, exception):
        if isinstance(exception, MakeRedirectException):
            redirect_url= request.META['PATH_INFO']
            return HttpResponsePermanentRedirect(redirect_url)
