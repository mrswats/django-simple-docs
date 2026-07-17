# Django simple Docs

This is a django app to easily configure `drf_spectacular`.

## Instalation

Installing from PyPI:
```console
pip install django-simple-docs
```

Add the following settings in your project:

```python

INSTALLED_APPS = [
    ...,
    "django_simple_docs",
    "drf_spectacular",
    ...,
]

REST_FRAMEWORK = {
    ...,
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    ...,
}

```

And, finally, configure the URLs:

```python
urlpatterns = [
    ...,
    path("api/docs/", include("django_simple_docs.urls")),
    ...,
]
```

Now, you can go to `http://localhost:8000/api/docs/` and browse the OpenAPI docs in your browser.

## Rationale

This is a simply configured drf_spectacular package for quickly getting started
with having OpenAPI docs withour much fuss. If you need more customization,
this package is probably not for you.

## Virtual Environment

Create a virtual Environment

```
virtualenv .venv -p pytthon 3.14
source .venv/bin/activate
```

## Tests

Using pytest for Tests

```
python -m pytest
```

## Formatting and Linting

Using pre-commit for linting and formatting

```
pre-commit install
pre-commit run --all-files
```
