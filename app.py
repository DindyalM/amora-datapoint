import asyncio
import aiohttp
from bs4 import BeautifulSoup
from flask import Flask
import os

loop = asyncio.get_event_loop()
app = Flask(__name__)

async def get_img(dress_url):
    imgs = []
    async with aiohttp.ClientSession() as session:
        async with session.get(dress_url) as res:
            html_body = await res.text()
            soup = BeautifulSoup(html_body,'html.parser')
            dress_divs = soup.find_all("button", class_='product-slideshow__syte-button syte-discovery-modal')
            for divs in dress_divs:
                imgs.append(divs.get("data-image-src"))
            return imgs

async def get_urls(url):
    urls = []
    count = 0
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            html_body = await res.text()
            soup = BeautifulSoup(html_body,'html.parser')
            dress_divs= soup.find_all('div', class_='collection-list__product-tile')
            for div in dress_divs:
                if count  !=10:
                    urls.append(div.find('a').attrs['href'])
                    count = count +1
            return urls

async def fetch():   
    task = asyncio.create_task(get_urls("https://www.fashionnova.com/collections/dresses"))
    url_holder = await asyncio.gather(task)
    
    tasks,task = [],[]

    for url in url_holder[0]:
       url = "https://www.fashionnova.com"+url
       task = asyncio.create_task(get_img(url))
       tasks.append(task)
    
    return await asyncio.gather(*tasks)

@app.route("/")
def index():
   return loop.run_until_complete(fetch())
    
if __name__ == "__main__":
    app.run(debug=False,port=6969)   










