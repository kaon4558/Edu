import time
import asyncio

from pyppeteer import launch
from concurrent.futures import ProcessPoolExecutor
from urllib.parse import urlparse

WEBSITE_LIST = [
    'http://naver.com',
    'http://envato.com',
    'http://amazon.co.uk',
    'http://amazon.com',
    'http://facebook.com',
    'http://google.com',
    'https://python-guide-kr.readthedocs.io/ko/latest/',
    'https://git-scm.com/book/ko/v2/시작하기-Git-최초-설정',
    'http://google.co.uk',
    'http://internet.org',
    'http://gmail.com',
    'http://stackoverflow.com',
    'http://github.com',
    'http://heroku.com',
    'http://djangoproject.com',
    'http://rubyonrails.org',
    'http://basecamp.com',
    'http://trello.com',
    'http://yiiframework.com',
    'http://shopify.com',
    'http://airbnb.com',
    'http://instagram.com',
    'http://snapchat.com',
    'http://youtube.com',
    'http://daum.net',
    'http://yahoo.com',
    'http://live.com',
    'http://linkedin.com',
    'http://yandex.ru',
    'http://netflix.com',
    'http://wordpress.com',
    'http://bing.com',
]

start = time.time()

async def fetch(url):
    browser = await launch(headless=True, args=['--no-sandbox'])
    page = await browser.newPage()
    await page.setViewport(viewport={'width' : 1200, 'height' : 1200})
    await page.goto(f'{url}', {'waitUntil': 'load'})
    await page.screenshot({'path': f'/Users/hyon/Desktop/workspace/origin/{urlparse(url)[1]}.jpg', type : 'jpeg', 'quality' : 75})
    await browser.close()


if __name__ =='__main__':
    executor = ProcessPoolExecutor(max_workers=4)
    event_loop = asyncio.get_event_loop()
    try:
        for url in WEBSITE_LIST:
            event_loop.run_until_complete(fetch(url))
    finally:
        event_loop.close()

    print(f'{time.time()-start} seconds.')
