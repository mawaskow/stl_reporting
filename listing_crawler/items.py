# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class lstngItem(Item):
	link = Field()
	title = Field()
	#listing_type = Field()
	#listing_area = Field()
	latitude = Field()
	longitude = Field()
	address = Field()
	description = Field()
	address_hidden = Field()
	#publication_date = Field()
	scrape_date = Field()
	#scrape_info = Field()
	reserve_prompt = Field()

	pass

class insideAirbnbItem(Item):
	lstng_id = Field()
	listing_url = Field()
	scrape_id = Field()
	last_searched = Field()
	last_scraped = Field()
	source = Field()
	name = Field()
	description = Field()
	host_id = Field()
	host_url = Field()
	host_name = Field()
	host_since = Field()
	host_location = Field()
	host_neighbourhood = Field()
	host_listings_count = Field()
	host_total_listings_count = Field()
	neighbourhood = Field()
	latitude = Field()
	longitude = Field()
	property_type = Field()
	room_type = Field()
	accommodates = Field()
	bathrooms = Field()
	bedrooms = Field()
	beds = Field()
	price = Field()
	estimated_occupancy_l365d = Field()
	estimated_revenue_l365d = Field()
	calculated_host_listings_count = Field()
	calculated_host_listings_count_entire_homes = Field()
	calculated_host_listings_count_private_rooms = Field()
	calculated_host_listings_count_shared_rooms = Field()
	region_id = Field()
	region_name = Field()
	region_parent_id = Field()
	region_parent_name = Field()
	region_parent_parent_id = Field()
	region_parent_parent_name = Field()
	
	pass
