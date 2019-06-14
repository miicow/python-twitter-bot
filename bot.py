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


def scrape_coursera():
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6)'
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'
    }

    r = requests.get('https://blog.coursera.org', headers=HEADERS)
    tree = fromstring(r.content)

    links = tree.xpath('//div[@class="recent"]//div[@class="title"]/a/@href')
    print(links)


scrape_coursera()
