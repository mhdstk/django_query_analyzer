=====
Heading
=====
Description here
Detailed documentation is in the "docs" directory.
Quick start
-----------
1. Add "django_query_analyzer" to your INSTALLED_APPS setting like this::
INSTALLED_APPS = [
        ...
        'django_query_analyzer',
    ]
2. Include the polls URLconf in your project urls.py like this::
path('', include('django_query_analyzer.urls')),
3. Run `python manage.py migrate` to create the polls models.
4. Start the development server and visit http://127.0.0.1:8000/query-analyzer/