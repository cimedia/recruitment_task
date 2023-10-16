import re


class HTMLParser:
    @staticmethod
    def remove_html_tags(html: str):
        return re.sub("<.*?>", "", html)
