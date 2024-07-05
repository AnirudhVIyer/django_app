from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PhotoForm
from .models import Photo


@login_required
def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            return redirect('photo_list')
    else:
        form = PhotoForm()
    return render(request, 'photo_upload.html', {'form': form})

@login_required
def photo_list(request):
    photos = Photo.objects.filter(user=request.user)
    return render(request, 'photo_list.html', {'photos': photos})

@login_required
def delete_photo(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id, user=request.user)
    if request.method == "POST":
        photo.delete()
        return redirect('photo_list')
    return render(request, 'confirm_delete.html', {'photo': photo})


