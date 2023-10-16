import pytest

from services.text_processor import TextProcessor


@pytest.fixture
def text_processor():
    return TextProcessor()


def test_remove_punctuation(text_processor):
    text = "Hello, world!"
    expected_output = "Hello world"
    assert text_processor.remove_punctuation(text) == expected_output


def test_clean_text(text_processor):
    text = "Hello,&nbsp;world!"
    expected_output = "Hello world"
    assert text_processor.clean_text(text) == expected_output


def test_count_word_frequencies(text_processor):
    words = ["hello", "world", "hello", "world", "hello"]
    expected_output = [("hello", 3), ("world", 2)]
    assert text_processor.count_word_frequencies(words) == expected_output
