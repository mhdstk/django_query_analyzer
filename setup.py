from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))
with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()


setup(
    name="django_query_analyzer",
    version="0.0.13",
    description="Python package for query analysis and monitoring in Django",
    long_description_content_type="text/markdown",
    long_description=long_description,
    author="Muhammed Shaheen",
    author_email="muhammedshaheen.tkb@gmail.com",
    keywords=['python', 'django', 'query', 'sql-query', 'query-analyzer', 'query-monitoring',
              'query-analysis', 'django-query-analyzer', 'django-query-monitoring', 'django-query-analysis'],
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Django",
    ],

)
