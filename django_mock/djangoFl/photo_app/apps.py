from django.apps import AppConfig


class PhotoAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'photo_app'


class PhotoAppConfig(AppConfig):
    name = 'photo_app'

    def ready(self):
        import photo_app.signals  # Ensure signals are imported and registered
