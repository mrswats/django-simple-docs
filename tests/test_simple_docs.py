from http import HTTPStatus

import pytest
from django.apps import apps
from django.test import Client
from django.urls import reverse


def test_django_simple_docs_startup_checks_drf_spectacular_is_installed(settings):
    settings.INSTALLED_APPS.remove("drf_spectacular")

    simple_docs_app = apps.get_app_config("django_simple_docs")

    with pytest.raises(AssertionError) as exc:
        simple_docs_app.ready()

    assert exc.value.args == ("drf_spectacular must be added as one of your apps",)


def test_django_simple_docs_startup_checks_drf_schema_is_configured(settings):
    settings.REST_FRAMEWORK["DEFAULT_SCHEMA_CLASS"] = "foo.bar"

    simple_docs_app = apps.get_app_config("django_simple_docs")

    with pytest.raises(AssertionError) as exc:
        simple_docs_app.ready()

    assert exc.value.args == (
        (
            "'DEFAULT_SCHEMA_CLASS' in 'REST_FRAMEWORK' settings "
            "should be 'drf_spectacular.openapi.AutoSchema'"
        ),
    )


@pytest.mark.parametrize(
    "url_name, resolved_url",
    [
        ("docs-html", "/"),
        ("docs-schema", "/openapi.yaml"),
    ],
)
def test_django_simple_docs_urls(url_name: str, resolved_url: str) -> None:
    assert reverse(url_name) == resolved_url


@pytest.mark.parametrize(
    "url_name",
    [
        "docs-html",
        "docs-schema",
    ],
)
def test_django_simple_docs_status_code(client: Client, url_name: str) -> None:
    response = client.get(reverse(url_name))
    assert response.status_code == HTTPStatus.OK


@pytest.mark.parametrize(
    "url_name, content",
    [
        ("docs-html", "<title>Swagger</title>"),
        ("docs-schema", "openapi: 3.0.3"),
    ],
)
def test_django_simple_docs_response(client: Client, url_name: str, content) -> None:
    response = client.get(reverse(url_name))
    assert content in response.content.decode()
