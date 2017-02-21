__author__ = 'aniruddha'
from functools import wraps
from datetime import timedelta,datetime
from .exceptions import AuthenticationFailure
import pytz



def login_required(func):
    @wraps(func)
    def decorator(*args,**kwargs):
        request = args[1]
        if request.auth == None:
            raise AuthenticationFailure('Token is not present. Unauthorised access')
        else:
            token = request.auth
            utc_now = datetime.utcnow()
            utc_now = utc_now.replace(tzinfo=pytz.utc)
            if token.created < utc_now - timedelta(days=60):
                token.delete()
                raise  AuthenticationFailure('Token has expired')
            else:
                return func(*args, **kwargs)
    return decorator

