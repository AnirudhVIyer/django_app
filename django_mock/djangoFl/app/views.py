from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.urls import reverse
from django.shortcuts import redirect

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

@api_view(['GET'])
def welcome(requests):
    return redirect(reverse('welcome'))
