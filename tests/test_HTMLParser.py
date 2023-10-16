import pytest

from services.HTMLParser import HTMLParser


@pytest.fixture
def html_parser():
    return HTMLParser()


def test_remove_html_tags(html_parser):
    html = "<p>Hello, <b>world</b>!</p>"
    expected_output = "Hello, world!"

    assert html_parser.remove_html_tags(html=html) == expected_output
