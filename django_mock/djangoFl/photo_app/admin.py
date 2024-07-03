
# Register your models here.
from django.contrib import admin
from .models import Photo

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('user', 'description', 'uploaded_at')
    search_fields = ('user__email', 'description')
    list_filter = ('uploaded_at', 'user')

admin.site.register(Photo, PhotoAdmin)