__author__ = 'aniruddha'
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler
import logging


def QuizExceptionHandler(exc, context):
    logger = logging.getLogger("quiz_exceptions")
    # Call REST framework's default exception handler first,
    response = exception_handler(exc, context)
    if response is not None:
        logger.exception(exc.default_detail)
        response = {"status": "Error",
                    "error": {"code": exc.status_code,
                              "error": exc.default_detail,
                              "detail": exc.detail
                              }
                    }

    return Response(response)

class InvalidCredentials(APIException):
    status_code = 701
    default_detail = 'Invalid Credentials'

class InvalidInformation(APIException):
    status_code = 702
    default_detail = 'Incorrect or invalid Data'

class InvalidData(APIException):
    status_code = 703
    default_detail = 'Incorrect Post Data'

class ObjectDoesNotExist(APIException):
    status_code = 704
    default_detail = 'Object does not Exist'

