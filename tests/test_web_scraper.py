import pytest
from unittest.mock import patch

from services.web_scraper import WebScraper


@pytest.fixture
def web_scraper():
    return WebScraper()


@patch("requests.get")
def test_scrape_website(mock_get, web_scraper):
    url = "https://example.com"

    mocked_output = "<html><body><p>Hello, world!</p></body></html>"
    mock_get.return_value.text = mocked_output

    expected_output = "<p>Hello, world!</p>"

    assert web_scraper.scrape_website(url) == expected_output
    mock_get.assert_called_once_with(url)
