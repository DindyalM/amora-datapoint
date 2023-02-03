import asyncio
import aiohttp
from bs4 import BeautifulSoup
from flask import Flask
import json
import os
from flask_cors import CORS, cross_origin
from selenium import webdriver

loop = asyncio.get_event_loop()


async def fetch_sh():
    task = asyncio.create_task(get_urls_shein("https://ca.shein.com/Plus%20Size%20Dresses-c-1889.html"))
    img_sh = await asyncio.gather(task)
    return img_sh

async def get_urls_shein(url):
    img = []
    count = 0
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            html_body = await res.text()
            soup = BeautifulSoup(html_body,'html.parser')
            #print([tag.name for tag in soup.find_all("a")])
            dress_divs= soup.find_all("html")
            print(dress_divs)
            #for div in dress_divs:
             #   if count  !=10:
              #      img.append(div.find('a').attrs['href'])
               #     count = count +1
            return dress_divs

if __name__ == "__main__":
   loop.run_until_complete(fetch_sh())