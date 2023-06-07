from django.contrib.sessions.models import Session
from django.conf import settings

# auth middleware
# admin access middleware
# response middleware
# OneSessionPerUserMiddleware


class ExampleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
        self.count_requests = 0
        self.count_exceptions = 0

    def __call__(self, request, *args, **kwargs):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        
        self.count_requests += 1
        response = self.get_response(request)

        # if settings.DEBUG:
        #     print("===================================================== After response")
        # Code to be executed for each request/response after
        # the view is called.

        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        # This code is executed just before the view is called
        # if settings.DEBUG:
        #     print("===================================================== before view is called")
        pass

    def process_exception(self, request, exception):
        # This code is executed if an exception is raised
        self.count_exceptions += 1
        # if settings.DEBUG:
        #     print(f"Encountered {self.count_exceptions} exceptions so far")
        #     print("===================================================== exception raised")
        pass

    def process_template_response(self, request, response):
        # This code is executed if the response contains a render() method
        # if settings.DEBUG:
        #     print("===================================================== After render() method call...")
        return response
    