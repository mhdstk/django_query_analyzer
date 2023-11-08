from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import QueryAnalyzer
from django.conf import settings


@receiver(post_save, sender=QueryAnalyzer)
def cleanup_query_analyzers(sender, instance, created, **kwargs):
    max_records = getattr(settings, 'MAX_QUERY_ANALYZER_RECORDS', 50)
    num_records = QueryAnalyzer.objects.count()

    if num_records >= max_records:
        QueryAnalyzer.objects.filter(id__in=list(
            QueryAnalyzer.objects.values_list('pk', flat=True)[:num_records - max_records])).delete()
