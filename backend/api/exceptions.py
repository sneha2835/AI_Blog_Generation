from rest_framework.views import exception_handler
from rest_framework.response import Response
import sys
import traceback

def custom_exception_handler(exc, context):
    # Call default handler
    response = exception_handler(exc, context)

    if response is None:
        # This is an unhandled error → return JSON instead of HTML
        return Response({
            "error": str(exc),
            "type": str(type(exc).__name__),
            "trace": traceback.format_exc()
        }, status=500)

    return response
