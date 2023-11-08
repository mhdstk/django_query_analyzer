from django.db import models


class QueryAnalyzer(models.Model):
    method = models.CharField(max_length=10)
    path = models.CharField(max_length=255)
    query_count = models.PositiveIntegerField()
    db_time = models.FloatField()
    total_time = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    query_list = models.JSONField()

    def __str__(self):
        return f"{self.method} {self.path}"
