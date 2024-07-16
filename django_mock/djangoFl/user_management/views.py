from django.contrib.auth import login, authenticate, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .forms import CustomUserCreationForm
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework import status

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.name
        token['email'] = user.email
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data.update({'user': {'username': self.user.name, 'email': self.user.email}})
        return data

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)



@csrf_exempt
def api_register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print(f"Registration data received: {data}")  # Debug statement
            form = CustomUserCreationForm(data)
            if form.is_valid():
                form.save()
                email = form.cleaned_data.get('email')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(request, email=email, password=raw_password)
                if user is not None:
                    login(request, user)
                    return JsonResponse({'message': 'Registration successful'}, status=201)
                return JsonResponse({'message': 'User authentication failed'}, status=400)
            print(f"Form errors: {form.errors}")  # Debug statement
            return JsonResponse({'errors': form.errors}, status=400)
        except Exception as e:
            print(f'Error: {e}')  # Debug statement
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=405)



@csrf_exempt
def api_login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        user = authenticate(request, email=email, password=password)
        print(email)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful', 'user': {'username':user.name, 'email':user.email}}, status=200)
        return JsonResponse({'error': 'Invalid credentials'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def api_logout(request):
    logout(request)
    return JsonResponse({'message': 'Logout successful'}, status=200)

def api_welcome(request):
    return JsonResponse({'message': 'Welcome to the BDR APP'}, status=200)

def api_user_home(request):
    if request.user.is_authenticated:
        user = request.user
        return JsonResponse({'message': f'Welcome {user.username}', 'user': {'name': user.username, 'email': user.email}}, status=200)
    return JsonResponse({'error': 'User not authenticated'}, status=401)
