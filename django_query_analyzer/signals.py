from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import QueryAnalyzer
from django.conf import settings


@receiver(post_save, sender=QueryAnalyzer)
def cleanup_query_analyzers(sender, instance, created, **kwargs):
    max_records = getattr(settings, "MAX_QUERY_ANALYZER_RECORDS", 50)
    objects = QueryAnalyzer.objects.all().order_by("-id")
    num_records = objects.count()

    if num_records >= max_records:
        point_to_remove = abs(max_records - num_records)
        copy_of_objects = objects[:point_to_remove]
        ids_to_delete = copy_of_objects.values_list("id", flat=True)
        objects.filter(id__in=ids_to_delete).delete()