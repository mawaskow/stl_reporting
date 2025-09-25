import scrapy
import json
import hashlib
import os
from pathlib import Path

class airBnBSpider(scrapy.Spider):
    name = "airbnb"

    async def start(self):
        urls = [
            "https://www.airbnb.ie/s/Galway-City/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJFTz2pOyWW0gRo4neikAvIJ8&acp_id=900edf7c-9c2e-4bda-a431-d90ede6f10b3&date_picker_type=calendar&source=structured_search_input_header&search_type=filter_change&query=Galway%20City&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2025-10-01&monthly_length=3&monthly_end_date=2026-01-01&search_mode=regular_search&price_filter_input_type=2&channel=EXPLORE&room_types%5B%5D=Entire%20home%2Fapt&selected_filter_order%5B%5D=room_types%3AEntire%20home%2Fapt&update_selected_filters=false",
            #"https://www.airbnb.ie/s/Galway-City/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJFTz2pOyWW0gRo4neikAvIJ8&acp_id=900edf7c-9c2e-4bda-a431-d90ede6f10b3&date_picker_type=flexible_dates&flexible_trip_lengths%5B%5D=weekend_trip&source=structured_search_input_header&search_type=filter_change&query=Galway%20City&monthly_start_date=2025-10-01&monthly_length=3&monthly_end_date=2026-01-01&search_mode=regular_search&price_filter_input_type=2&price_filter_num_nights=2&channel=EXPLORE&room_types%5B%5D=Entire%20home%2Fapt&selected_filter_order%5B%5D=room_types%3AEntire%20home%2Fapt&update_selected_filters=false",
            #"https://www.airbnb.ie/s/Galway-City/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJFTz2pOyWW0gRo4neikAvIJ8&acp_id=900edf7c-9c2e-4bda-a431-d90ede6f10b3&date_picker_type=flexible_dates&source=structured_search_input_header&search_type=unknown&query=Galway%20City&monthly_start_date=2025-10-01&monthly_length=3&monthly_end_date=2026-01-01&search_mode=regular_search&price_filter_input_type=2&price_filter_num_nights=2&channel=EXPLORE&room_types%5B%5D=Entire%20home%2Fapt&selected_filter_order%5B%5D=room_types%3AEntire%20home%2Fapt&update_selected_filters=false&flexible_trip_lengths%5B%5D=one_week",
            #"https://www.airbnb.ie/s/Galway-City/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJFTz2pOyWW0gRo4neikAvIJ8&acp_id=900edf7c-9c2e-4bda-a431-d90ede6f10b3&date_picker_type=flexible_dates&source=structured_search_input_header&search_type=unknown&query=Galway%20City&monthly_start_date=2025-10-01&monthly_length=3&monthly_end_date=2026-01-01&search_mode=regular_search&price_filter_input_type=2&price_filter_num_nights=5&channel=EXPLORE&room_types%5B%5D=Entire%20home%2Fapt&selected_filter_order%5B%5D=room_types%3AEntire%20home%2Fapt&update_selected_filters=false&flexible_trip_lengths%5B%5D=one_month"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")


'''
get urls for all pages of results
get all entities of class="rfexzly atm_9s_1ulexfb atm_7l_1j28jx2 atm_e2_1osqo2v dir dir-ltr" or target="listing_*"
maybe selenium to get all the results then scrapy to work with the collected urls?
construct the urls based on the target="listing_*" value
remove duplicates once all results have been gathered across all urls
follow all the links and extract all the data into the items
'''

'''
scrapy shell
url = "https://www.airbnb.ie/s/Galway-City/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJFTz2pOyWW0gRo4neikAvIJ8&acp_id=900edf7c-9c2e-4bda-a431-d90ede6f10b3&date_picker_type=calendar&source=structured_search_input_header&search_type=filter_change&query=Galway%20City&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2025-10-01&monthly_length=3&monthly_end_date=2026-01-01&search_mode=regular_search&price_filter_input_type=2&channel=EXPLORE&room_types%5B%5D=Entire%20home%2Fapt&selected_filter_order%5B%5D=room_types%3AEntire%20home%2Fapt&update_selected_filters=false"
request = scrapy.Request(url)
fetch(request)
response
response.selector.xpath("//div")
'''