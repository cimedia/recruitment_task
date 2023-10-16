import os

from services.file_saver import FileSaver
from services.html_parser import HTMLParser
from services.text_processor import TextProcessor
from services.web_scraper import WebScraper


def main():
    URL = os.getenv("URL")

    html_content = WebScraper.scrape_website(URL)

    parsed_html = HTMLParser.remove_html_tags(html=html_content)
    text_processor = TextProcessor()

    clean_text = text_processor.clean_text(parsed_html)
    words = clean_text.split()

    word_frequencies = text_processor.count_word_frequencies(words)
    most_frequently_used_words = word_frequencies[:10]

    FileSaver.save_to_file(most_frequently_used_words)


if __name__ == "__main__":
    main()
