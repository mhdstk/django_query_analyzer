from django.shortcuts import render
from .models import QueryAnalyzer

def query_analyzer_list(request):
    limit = request.GET.get("limit", "All")

    query_analyzers = QueryAnalyzer.objects.all().order_by("-created_at")

    if limit.isdigit():
        query_analyzers = query_analyzers[: int(limit)]
    return render(
        request,
        "django_query_analyzer/django_query_analyzer.html",
        {"query_analyzers": query_analyzers, "limit": limit},
    )