import re

import requests


class WebScraper:
    @staticmethod
    def scrape_website(url):
        try:
            response = requests.get(url)
            response.raise_for_status()

            body_content = re.search(
                r"<body[^>]*>(.*)</body>", response.text, re.DOTALL
            )

            return body_content.group(1)

        except requests.exceptions.HTTPError as errh:
            print("HTTP Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            print("Connection Error:", errc)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
        except requests.exceptions.RequestException as err:
            print("Other Error:", err)
