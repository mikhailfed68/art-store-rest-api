from django.http import Http404
from django.conf import settings
from django.urls import reverse

from common.utlis import array_has_regex


class IsApiRequest:
    @staticmethod
    def is_api_request(request):
        path = request.path_info.lower()
        api_root = reverse("api-root").lower()
        return path.startswith(api_root)


class HeaderSessionMiddleware(IsApiRequest):
    def __init__(self, get_response) -> None:
        self._get_response = get_response

    def __call__(self, request):
        header_session_id = request.headers.get('Session-Id')

        # если заголовок в запрсое существует, то превращаем его в куку
        if header_session_id:
            request.COOKIES['sessionid'] = header_session_id

        response = self._get_response(request)

        if  request.method != 'OPTIONS':
            if self.is_api_request(request) and response.user.is_anonymous:
                # получаем Set-Cookie (установленную в SessionMiddleware)
                # и значение sessionid
                set_cookie_object = response.cookies.get('sessionid')
                if set_cookie_object:
                    session_id = set_cookie_object.value

                    # устанавливаем заголовок в ответе и удаляем куку
                    response.headers['Session-Id'] = session_id
                    response.delete_cookie('sessionid')
                return response
        return response

 
class SetUserResponseMiddleware(IsApiRequest):
    def __init__(self, get_response) -> None:
        self._get_response = get_response

    def __call__(self, request):
        response = self._get_response(request)
    
        if self.is_api_request(request):
            response.user = request.user
            return response
        return response


class NotFoundMiddleware:
    def __init__(self, get_response) -> None:
        self._get_response = get_response

    def __call__(self, request):

        if not array_has_regex(request.path_info, settings.NOT_FOUND_IGNORE_PATHS) and request.user.is_anonymous:
            raise Http404('Not Found')

        return self._get_response(request)
