class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        logged_data = {
            'response_status_code': response.status_code,
            'response_content': response.content,
            'requested_url': request.path,
            'requested_method': request.method,
            'requested_data': request.GET
        }
        print(logged_data)
        return response
