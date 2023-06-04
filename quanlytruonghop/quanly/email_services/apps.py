from django.apps import AppConfig


class EmailServicesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'email_services'

    def ready(self) -> None:
        import email_services.signals