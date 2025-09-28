import scrapy
import json
import hashlib
import os
from pathlib import Path
from ..items import lstngItem
import datetime
import time

cwd = os.getcwd()
output_dir = cwd+"/scraping_outputs"

urls = []
with open(output_dir+"/booking_connemara_urls.txt", "r") as f:
    for line in f:
        urls.append(line.strip())

class bookingSpider(scrapy.Spider):
    name = "booking"

    async def start(self):
        for url in urls:#[:5]:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        time.sleep(1)
        address_obscured=False
        address_msg = response.selector.xpath('//div[@class="dcf8588897"]/text()').get()
        if address_msg:
            if address_msg.split(" ")[0] == "After":
                address_obscured=True 
        lst_item = lstngItem()
        lst_item['link'] = response.url
        lst_item['title'] = response.selector.xpath('//h2[contains(@class,"pp-header__title")]/text()').get()
        lst_item['reserve_prompt'] = response.selector.xpath('//span[@class="bui-button__text"]/text()').get()
        #lst_item['listing_type'] = 
        loc = response.selector.xpath('//a[@data-atlas-latlng]/@data-atlas-latlng').get()
        if loc:
            lat = loc.split(",")[0]
            lon = loc.split(",")[1]
        else:
            lat = None
            lon = None
        lst_item['latitude'] = lat
        lst_item['longitude'] = lon
        lst_item['address'] = response.selector.xpath('//div[@class="b99b6ef58f cb4b7a25d9 b06461926f"]/text()').get()
        lst_item['address_hidden'] = address_obscured
        #lst_item['listing_area'] = ""
        lst_item['description'] = response.selector.xpath('//p[@data-testid="property-description"]/text()').get()
        #lst_item['publication_date'] = 
        lst_item['scrape_date'] = datetime.date.today()
        #lst_item['scrape_info'] = ""
        yield lst_item

# https://scrapfly.io/blog/posts/how-to-scrape-bookingcom
