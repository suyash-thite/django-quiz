__author__ = 'aniruddha'
from functools import wraps
from .exceptions import AuthenticationFailure



def login_required(func):
    @wraps(func)
    def decorator(*args,**kwargs):
        request = args[1]
        if request.auth == None:
            raise AuthenticationFailure('Token is not present. Unauthorised access')
        else:
            return func(*args, **kwargs)
    return decorator