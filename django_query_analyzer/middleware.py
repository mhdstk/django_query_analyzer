import time

from django.conf import settings
from django.db import connection

from .models import QueryAnalyzer

# ANSI color escape codes
GREEN = "\033[32m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
RESET = "\033[0m"

DOUBLE_LINE = "=" * 40


class QueryAnalyzerMiddleware:

    enable_console = getattr(settings, 'ENABLE_LOGGING_TO_TERMINAL', True)

    def __init__(self, get_response):
        self.get_response = get_response

    def print_query(self, request, query_count, db_time, total_time):
        # Print a double line as a separator
        print(f"{DOUBLE_LINE}")

        # Log the query analysis with colors
        print(f"{GREEN}API Request: {request.method} {request.path}{RESET}")
        print(f"{CYAN}Query Count: {query_count}{RESET}")
        print(f"{YELLOW}Database Time: {db_time:.3f} ms{RESET}")
        print(f"{YELLOW}Total Time: {total_time:.3f} s{RESET}")

        print(f"{DOUBLE_LINE}")

    def __call__(self, request):
        # exclude admin urls
        if request.path.startswith('/admin/'):
            return self.get_response(request)
        # exclude the path /query-analyzer/
        if request.path.startswith('/query-analyzer/'):
            return self.get_response(request)
        #  exclude swagger urls
        if request.path.startswith('/swagger/'):
            return self.get_response(request)

        if request.path.startswith('/docs/'):
            return self.get_response(request)

        if request.path.startswith('/redoc/'):
            return self.get_response(request)

        if request.path.startswith('/favicon.ico'):
            return self.get_response(request)

        if request.path.startswith('/static/'):
            return self.get_response(request)

        query_list = []
        # Start timing the request processing
        start_time = time.time()

        response = self.get_response(request)

        # Calculate the time taken for the request
        total_time = time.time() - start_time

        # Analyze and log database queries
        query_count = len(connection.queries)
        # print(connection.queries)
        db_time = sum(float(query['time']) for query in connection.queries)

        # Capture the executed queries
        for query in connection.queries:
            query_list.append({
                'sql': query['sql'],
                'time': query['time'],
            })

        if self.enable_console:
            # Print on the terminal
            self.print_query(request, query_count, db_time, total_time)

        # Store the query analysis in the database
        QueryAnalyzer.objects.create(
            method=request.method,
            path=request.path,
            query_count=query_count,
            db_time=db_time,
            total_time=total_time,
            query_list=query_list
        )

        return response
