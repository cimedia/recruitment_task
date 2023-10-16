import os

from services.FileSaver import FileSaver
from services.HTMLParser import HTMLParser
from services.TextProcessor import TextProcessor
from services.WebScraper import WebScraper


def main():
    URL = os.getenv("URL")

    html_content = WebScraper.scrape_website(URL)

    html_parser = HTMLParser.remove_html_tags(html=html_content)
    text_processor = TextProcessor()

    clean_text = text_processor.clean_text(html_parser)
    words = clean_text.split()

    word_frequencies = text_processor.count_word_frequencies(words)
    most_frequently_used_words = word_frequencies[:10]

    FileSaver.save_to_file(most_frequently_used_words)


if __name__ == "__main__":
    main()
