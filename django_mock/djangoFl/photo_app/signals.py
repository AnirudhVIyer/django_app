from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Photo

@receiver(post_delete, sender=Photo)
def delete_image_file(sender, instance, **kwargs):
    # Ensure that the instance has an image and it's stored in S3
    if instance.image:
        instance.image.delete(save=False)