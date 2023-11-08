# Django Query Analyzer

Django Query Analyzer is a Django app that allows you to monitor and analyze the database queries executed by your Django application.

## Installation

1. Add "django_query_analyzer" to your `INSTALLED_APPS` setting in your Django project's `settings.py`:

   ```python
   INSTALLED_APPS = [
       ...
       'django_query_analyzer',
   ]
   ```

2. Add "django_query_analyzer.middleware.QueryAnalyzerMiddleware" to your project's `MIDDLEWARE` list in `settings.py`:

   ```python
   MIDDLEWARE = [
       ...
       "django_query_analyzer.middleware.QueryAnalyzerMiddleware",
   ]
   ```

3. Register the query analyzer URL patterns in your project's `urls.py`:

   ```python
   from django.urls import path, include

   urlpatterns = [
       ...
       path("query-analyzer/", include("django_query_analyzer.urls")),
   ]
   ```

4. Run the following command to create the necessary database tables for the "django_query_analyzer" package:

   ```bash
   python manage.py migrate
   ```

## Usage

1. Start your Django development server:

   ```bash
   python manage.py runserver
   ```

2. Visit the query analyzer dashboard at [http://127.0.0.1:8000/query-analyzer/](http://127.0.0.1:8000/query-analyzer/) in your web browser.

## Configuration

By default, the query analyzer stores the last 50 executed queries. If you want to control this number, you can add the `MAX_QUERY_ANALYZER_RECORDS` setting to your project's `settings.py`. For example, to store the last 100 queries, add the following line to your settings.py:

```python
MAX_QUERY_ANALYZER_RECORDS = 100
```

## Excluded Paths

By default, the query analyzer excludes URLs that start with `/admin/`, `/swagger/`, and `/docs/` from its analysis. More control over excluded paths may be available in future updates.
