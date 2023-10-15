import os
import re
import requests
import string

URL = os.getenv("URL")


def remove_html_tags(html: str):
    return re.sub("<.*?>", "", html)


def remove_punctuation(text: str):
    translator = str.maketrans("", "", string.punctuation)
    text_without_punctuation = text.translate(translator)
    return text_without_punctuation


def count_word_frequencies(_words: list[str]):
    _word_frequencies = {}
    for word in _words:
        if word in _word_frequencies:
            _word_frequencies[word] += 1
        else:
            _word_frequencies[word] = 1

    sorted_word_frequencies = sorted(
        _word_frequencies.items(), key=lambda x: x[1], reverse=True
    )
    return sorted_word_frequencies


def save_to_file(_word_frequencies, filename="results.txt"):
    try:
        with open(filename, "w") as file:
            for word, freq in _word_frequencies:
                file.write(f"{word}: {freq}\n")
    except Exception as e:
        print(f"An error occurred while saving the file: {str(e)}")


try:
    response = requests.get(URL)
    response.raise_for_status()

    body_content = re.search(
        r"<body[^>]*>(.*)</body>", response.text, re.DOTALL
    )

    clean_text = remove_html_tags(body_content.group(1))
    clean_text = clean_text.replace("&nbsp;", " ")
    clean_text = remove_punctuation(clean_text)
    clean_text = re.sub(r"\s+", " ", clean_text)
    words = clean_text.split()

    word_frequencies = count_word_frequencies(words)
    most_frequently_used_words = word_frequencies[:10]
    save_to_file(most_frequently_used_words)

    # print(most_frequently_used_words)

except requests.exceptions.HTTPError as errh:
    print("Błąd HTTP:", errh)
except requests.exceptions.ConnectionError as errc:
    print("Błąd połączenia:", errc)
except requests.exceptions.Timeout as errt:
    print("Błąd timeout:", errt)
except requests.exceptions.RequestException as err:
    print("Inny błąd:", err)
