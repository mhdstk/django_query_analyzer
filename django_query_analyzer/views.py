from django.shortcuts import render
from django.core.cache import cache



def query_analyzer_list(request):
    limit = request.GET.get("limit", "All")
    query_analyzers = cache.get("query_analyzer_cache")
    query_analyzers = sorted(
        query_analyzers, key=lambda x: x["timestamp"], reverse=True
    )
    if limit.isdigit():
        query_analyzers = query_analyzers[: int(limit)]
    return render(
        request,
        "django_query_analyzer/django_query_analyzer.html",
        {"query_analyzers": query_analyzers, "limit": limit},
    )
