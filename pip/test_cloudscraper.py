import cloudscraper

scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance
# Or: scraper = cloudscraper.CloudScraper()  # CloudScraper inherits from requests.Session
#print(scraper.get("http://example.com").text)  # => "<!DOCTYPE html><html><head>..."

import cloudscraper

proxies = {"http": "http://venus:8124", "https": "http://venus:8124"}
text = scraper.get("https://news.ycombinator.com", proxies=proxies).text
print(text)

