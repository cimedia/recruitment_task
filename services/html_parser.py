import re


class HTMLParser:
    @staticmethod
    def remove_html_tags(html: str):
        return re.sub("<.*?>", "", html)

    @staticmethod
    def remove_html_tags_v2(html: str):
        tag = False
        quote = False
        output = []
        for ch in html:
            if ch == '<' and not quote:
                tag = True
            elif ch == '>' and not quote:
                tag = False
            elif (ch == '"' or ch == "'") and tag:
                quote = not quote
            elif not tag:
                output.append(ch)

        return "".join(output)
