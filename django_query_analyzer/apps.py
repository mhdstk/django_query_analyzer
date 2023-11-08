from django.apps import AppConfig


class QueryAnalyzerAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "django_query_analyzer"

    def ready(self):
        import django_query_analyzer.signals
