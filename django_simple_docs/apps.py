from django.apps import AppConfig
from django.conf import settings


class SimpleDocsConfig(AppConfig):
    name = "django_simple_docs"

    def ready(self) -> None:
        assert (
            "drf_spectacular" in settings.INSTALLED_APPS
        ), "drf_spectacular must be added as one of your apps"
        assert (
            settings.REST_FRAMEWORK["DEFAULT_SCHEMA_CLASS"] == "drf_spectacular.openapi.AutoSchema"
        ), (
            "'DEFAULT_SCHEMA_CLASS' in 'REST_FRAMEWORK' settings "
            "should be 'drf_spectacular.openapi.AutoSchema'"
        )
