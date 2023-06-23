import string
import random

class URLShortener:
    def __init__(self):
        self.mapping = {}
        self.characters = string.ascii_letters + string.digits
        self.base_url = "http://short.com/"

    def shorten_url(self, original_url):
        if original_url in self.mapping:
            return self.mapping[original_url]

        short_code = self.generate_short_code()
        short_url = self.base_url + short_code
        self.mapping[original_url] = short_url
        return short_url

    def generate_short_code(self):
        short_code = ''.join(random.choice(self.characters) for _ in range(6))
        return short_code

    def get_original_url(self, short_url):
        for original_url, shortened in self.mapping.items():
            if shortened == short_url:
                return original_url
        return None

# Example usage
url_shortener = URLShortener()

original_url = "https://www.example.com/some/long/url"
short_url = url_shortener.shorten_url(original_url)
print("Shortened URL:", short_url)

retrieved_url = url_shortener.get_original_url(short_url)
print("Original URL:", retrieved_url)
