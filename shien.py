import asyncio
import aiohttp
from bs4 import BeautifulSoup
from flask import Flask
import json
import os
from flask_cors import CORS, cross_origin
from selenium import webdriver

#   task = asyncio.create_task(get_urls_shein("https://ca.shein.com/Plus%20Size%20Dresses-c-1889.html"))
  #  img_sh = await asyncio.gather(task)
   # return img_sh

#async def get_urls_shein(url):
 #   img = []
  #  count = 0
   # async with aiohttp.ClientSession() as session:
    #    async with session.get(url) as res:
     #       html_body = await res.text()
      #      soup = BeautifulSoup(html_body,'html.parser')
            #print([tag.name for tag in soup.find_all("a")])
       #     dress_divs= soup.find_all("html")
        #    print(dress_divs)
            #for div in dress_divs:
             #   if count  !=10:
              #      img.append(div.find('a').attrs['href'])
               #     count = count +1
     #       return dress_divs

loop = asyncio.get_event_loop()

async def fetch_sh(browser):
        browser.get("https://www.shopcider.com/collection/dress?link_url=https%3A%2F%2Fm.shopcider.com%2Fcollection%2Fdress&operationpage_title=homepage&operation_position=4&operation_type=category&operation_content=Dresses&listSource=homepage%3Bcollection_dress%3B4")
        soup = BeautifulSoup(browser.page_source,"html.parser")
        return(soup.findAll("div"))
 
if __name__ == "__main__": 
    if(webdriver.Safari()):
        browser = webdriver.Safari()
    elif(webdriver.Chrome()):
        browser = webdriver.Chrome()
    
print(loop.run_until_complete(fetch_sh(browser)))
browser.close()

        
    