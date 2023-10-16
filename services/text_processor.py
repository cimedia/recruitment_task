import re
import string
from collections import defaultdict


class TextProcessor:
    def remove_punctuation(self, text: str):
        translator = str.maketrans("", "", string.punctuation)
        text_without_punctuation = text.translate(translator)
        return text_without_punctuation

    def clean_text(self, text: str):
        text = text.replace("&nbsp;", " ")
        text = self.remove_punctuation(text)
        text = re.sub(r"\s+", " ", text)
        return text

    def count_word_frequencies(self, words: list[str]):
        word_frequencies = defaultdict(int)
        for word in words:
            word_frequencies[word] += 1

        sorted_word_frequencies = sorted(
            word_frequencies.items(), key=lambda x: x[1], reverse=True
        )
        return sorted_word_frequencies
