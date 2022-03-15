from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse


def parse_payload(token):
    """
    验证token
    :param token:
    :return:
    """
    import jwt
    jwt_salt = "abcd1234567890!@#$%^&*()"
    result = {"status": False, "data": None, "error": None}
    try:
        verified_payload = jwt.decode(token, jwt_salt, "HS256")
    except jwt.exceptions.ExpiredSignatureError:
        result["error"] = "token已过期"
    except jwt.exceptions.DecodeError:
        result["error"] = "token认证失败"
    except jwt.exceptions.InvalidTokenError:
        result["error"] = "非法token"
    else:
        result["status"] = True
        result["data"] = verified_payload
    return result


class JwtAuthorizationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        """
        定义jwt验证的中间件
        :param request:
        :return:
        """
        if request.path_info == "/get_token/" and request.method == "POST":
            return
        elif request.path_info == "/get_token/" and request.method == "GET":
            authorization = request.META.get("HTTP_AUTHORIZATION", "")
            authorization_info = authorization.split()
            if not authorization_info:
                return JsonResponse({"error": "未获取到token", "status": False})
            elif authorization_info[0].lower() != "jwt":
                return JsonResponse({"error": "token认证方式错误", "status": False})
            elif len(authorization_info) == 1 or len(authorization_info) > 2:
                return JsonResponse({"error": "非法token", "status": False})
            token = authorization_info[1]
            print(token)
            result = parse_payload(token)
            if not result["status"]:
                return JsonResponse(result)
            request.user_info = result["data"]

