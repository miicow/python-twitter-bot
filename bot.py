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
