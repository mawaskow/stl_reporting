import scrapy
import json
import hashlib
import os
from pathlib import Path

cwd = os.getcwd()
output_dir = cwd+"/scraping_outputs"

class bookingSpider(scrapy.Spider):
    name = "booking"

    async def start(self):
        urls = [
            #"https://www.booking.com/searchresults.html?ss=Galway%2C+Ireland&sb_entire_place=1&efdco=1&label=gen173nr-10CAEoggI46AdIM1gEaGmIAQGYATO4ARfIAQzYAQPoAQH4AQGIAgGoAgG4As7losUGwAIB0gIkMDk1YWZkNzctZjQzNS00NzZjLTkxMWQtYjRlZWZmOWE5YzUz2AIB4AIB&sid=aa49af52a05a1df4bb25bdf70149b942&aid=304142&lang=en-us&sb=1&src_elem=sb&src=index&dest_id=-1502950&dest_type=city&ltfd=6%3A28%3A10-2025_11-2025_12-2025%3A1%3A&group_adults=2&no_rooms=1&group_children=0&nflt=ht_id%3D1200%3Bprivacy_type_no_date%3D3",
            "https://www.booking.com/searchresults.html?dest_id=-1502950;dest_type=city;nflt=ht_id%3D1200%3Bprivacy_type_no_date%3D3"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"{output_dir}/test.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")


'''
<span class="ca2ca5203b">Load more results</span>
data-testid="title-link"
'''
# https://scrapfly.io/blog/posts/how-to-scrape-bookingcom
