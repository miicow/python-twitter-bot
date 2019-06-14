import credential
from twitter import OAuth, Twitter
import requests
import random
import time

from lxml.html import fromstring
import nltk
nltk.download('punkt')


tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

oauth = OAuth(
    credential.ACCESS_TOKEN,
    credential.ACCESS_SECRET,
    credential.CONSUMER_KEY,
    credential.CONSUMER_SECRET
)
t = Twitter(auth=oauth)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6)'
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'
}


def extract_paragraphtext(paragraphs):
    """Extracts text from <p> elements and return a clean, tokenized random paragraph."""
    paragraphs = [paragraph.text_content()
                  for paragraph in paragraphs if paragraph.text_content()]
    paragraph = random.choice(paragraphs)
    return tokenizer.tokenize(paragraph)


def extract_text(para):
    """Returns a sufficiently-large random text from a tokenized paragraph,
    if such text exists. Otherwise, returns None."""

    for _ in range(10):
        text = random.choice(para)
        if text and 60 < len(text) < 210:
            return text

    return None


def scrape_coursera():
    """ Scrapes content from the Coursera blog."""

    url = 'https://blog.coursera.org'

    r = requests.get(url, headers=HEADERS)
    tree = fromstring(r.content)
    links = tree.xpath('//div[@class="recent"]//div[@class="title"]/a/@href')

    for link in links:
        r = requests.get(link, headers=HEADERS)
        blog_tree = fromstring(r.content)
        paragraphs = blog_tree.xpath('//div[@class="entry-content"]/p')
        paragraph = extract_paragraphtext(paragraphs)
        text = extract_text(paragraph)
        if not text:
            continue

        yield '"%s" %s' % (text, link)
