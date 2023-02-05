import asyncio
import aiohttp
from bs4 import BeautifulSoup
from flask import Flask
import json
import os
from flask_cors import CORS, cross_origin

loop = asyncio.get_event_loop()
app = Flask(__name__)

CORS(app, support_credentials=True)


async def get_img_fn(dress_url):
    imgs = []
    async with aiohttp.ClientSession() as session:
        async with session.get(dress_url) as res:
            html_body = await res.text()
            soup = BeautifulSoup(html_body,'html.parser')
            dress_divs = soup.find_all("button", class_='product-slideshow__syte-button syte-discovery-modal')
            for divs in dress_divs:
                imgs.append(divs.get("data-image-src"))
                imgs.append(dress_url)
            return imgs

async def get_urls_fn(url):
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

async def fetch_fn():   
    task = asyncio.create_task(get_urls_fn("https://www.fashionnova.com/collections/dresses"))
    url_holder = await asyncio.gather(task)
    
    j,jholder,tasks,task = [],[],[],[]

    for url in url_holder[0]:
       url = "https://www.fashionnova.com"+url
       task = asyncio.create_task(get_img_fn(url))
       tasks.append(task)
    
    j  = await asyncio.gather(*tasks)
    for i in j:
        jholder.append({"url":i[0],"url2":i[1]})
    return json.dumps(jholder)
#-------------------------------------------

async def fetch_urls_sh(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            html_body = await res.text()
            soup = BeautifulSoup(html_body,'html.parser')
            print(soup)
            #like this!
        #    for a in soup.find_all('a',class_="cider-link", href=True):
         #       context = str(a['href'])
          #      imgs.append(context)
           # ans = filter(lambda k: 'good' in k,list(set(imgs)))
           # ans = json.dumps(list(ans))
            #fetch_img_sh(ans)
        return "oohohh"

async def fetch_img_sh(url):
    imgs = []
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            html_body = await res.text()
            soup = BeautifulSoup(html_body,'html.parser')
            for a in soup.find_all('a',class_="zoom-image-container"):
                context = str(a['href'])      
                return "live"

async def fetch_sh():
    task = asyncio.create_task(fetch_urls_sh("https://www.shopcider.com/collection/dress"))
    url_holder = await asyncio.gather(task)
    
    return url_holder
    #j,jholder,tasks,task = [],[],[],[]

    #for url in url_holder[0]:
       #url = "https://www.fashionnova.com"+url
      # task = asyncio.create_task(get_img_fn(url))
     #  tasks.append(task)
    
    #j  = await asyncio.gather(*tasks)
    #for i in j:
     #   jholder.append({"url":i[0],"url2":i[1]})
    
    #return json.dumps(jholder)
    #imgs=[]
        
@app.route("/")
def index():
   res = loop.run_until_complete(fetch_fn())
   return res

@app.route("/cider")
def shein():
   res = loop.run_until_complete(fetch_sh())
   return res

if __name__ == "__main__":
    app.run(debug=True,port=6969)











