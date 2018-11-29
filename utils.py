from bs4 import BeautifulSoup
from database import Database
import requests


def make_soup(url):
    ''' Retrieves html code from url '''
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko)'
                             ' Version/11.1.2 Safari/605.1.15'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print('Oops, you\'ve come across status code error: %s' % str(response.status_code))

    return BeautifulSoup(response.content, "html.parser")
