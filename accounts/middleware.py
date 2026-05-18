from django.shortcuts import redirect

class AuthMiddleware:

    def __init__(self, get_response):

        self.get_response = get_response

    def __call__(self, request):
        print("Middleware Running")
        print(request.session.items())
        protected_urls = [
            '/dashboard/',
        ]

        if request.path in protected_urls:

            user_id = request.session.get('user_id')

            if not user_id:

                return redirect('/')

        response = self.get_response(request)

        return response