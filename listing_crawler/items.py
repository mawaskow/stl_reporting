# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class bnbItem(Item):
	link = Field()
	title = Field()
	listing_type = Field()
	listing_area = Field()
	latitude = Field()
	longitude = Field()
	address = Field()
	description = Field()
	publication_date = Field()
	scrape_date = Field()

	pass
