from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    route = [
        {
            'method':'get',
            'endpoint':'/notes',
            'body': None
        }
    ]

    return Response(route)

