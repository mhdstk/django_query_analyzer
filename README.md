# django_query_analyzer

## Examples of How To Use

Add "django_query_analyzer" to your INSTALLED_APPS setting like this

```python
    INSTALLED_APPS = [
        ...
        'django_query_analyzer',
    ]
```

Add "django_query_analyzer.middleware.QueryAnalyzerMiddleware" to your MIDDLEWARE

```python
MIDDLEWARE = [
    ...
    "django_query_analyzer.middleware.QueryAnalyzerMiddleware",
]
```

Register in urls.py

```python
path("", include("django_query_analyzer.urls")),
```

Run `python manage.py migrate` to create the django_query_analyzer models.

Start the development server and visit http://127.0.0.1:8000/query-analyzer/.

Excluded paths starting with ['/admin/', '/swagger/', '/docs/']
