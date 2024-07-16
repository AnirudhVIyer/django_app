from django.shortcuts import render

# Create your views here.
import base64
import io
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PhotoForm
from .models import Photo
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
import json
from rest_framework.decorators import api_view
from rest_framework import status
import uuid
import time



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_upload_photo(request):
    print(f"Received data: {request.data}")
    print(f"Received files: {request.FILES}")

    if 'image' not in request.data:
        return Response({'error': 'No image provided'}, status=status.HTTP_400_BAD_REQUEST)

    image_data = request.data['image']
    print(f"Raw image data: {image_data}")

    try:
        format, imgstr = image_data.split(';base64,')
        ext = format.split('/')[-1]
        img_data = base64.b64decode(imgstr)
        print(f"Image format: {format}, Image extension: {ext}")
    except (ValueError, TypeError) as e:
        print(f"Error decoding base64 image data: {e}")
        return Response({'error': 'Invalid image data'}, status=status.HTTP_400_BAD_REQUEST)

    # Generate a unique filename
    unique_filename = f"{uuid.uuid4().hex}_{int(time.time())}.{ext}"

    img_io = io.BytesIO(img_data)
    image_file = InMemoryUploadedFile(img_io, None, unique_filename, 'image/' + ext, len(img_data), None)
    
    data = request.data.copy()
    files = request.FILES.copy()
    files['image'] = image_file

    form = PhotoForm(data, files)
    if form.is_valid():
        photo = form.save(commit=False)
        photo.user = request.user
        photo.save()
        return Response({'message': 'Photo uploaded successfully'}, status=status.HTTP_200_OK)
    
    print(f"Form errors: {form.errors}")
    return Response({'errors': form.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_photo_list(request):
    photos = Photo.objects.filter(user=request.user)
    print(request.user)
    photo_list = [{'id': photo.id, 'image_url': photo.image.url, 'description': photo.description} for photo in photos]
    for photo in photos:
        print(photo.image.url)
    print(len(photo_list))
    return JsonResponse({'photos': photo_list}, status=200)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def api_delete_photo(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id, user=request.user)
    if request.method == "DELETE":
        photo.delete()
        return JsonResponse({'message': 'Photo deleted successfully'}, status=200)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

