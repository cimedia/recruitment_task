import pytest

from services.FileSaver import FileSaver


@pytest.fixture
def file_saver():
    return FileSaver()


def test_save_to_file(file_saver, tmp_path):
    word_frequencies = [("hello", 3), ("world", 2)]
    filename = tmp_path / "results.txt"
    file_saver.save_to_file(word_frequencies, filename)

    with open(filename, "r") as file:
        content = file.read()
        expected_output = "hello: 3\nworld: 2\n"
        assert content == expected_output
