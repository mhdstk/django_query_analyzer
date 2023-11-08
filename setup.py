from setuptools import setup, find_packages

setup(
    name="django_query_analyzer",
    version="0.0.7",
    description="Python package for query analysis and monitoring in Django",
    author="Muhammed Shaheen",
    author_email="muhammedshaheen.tkb@gmail.com",
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Django",
    ],

)
