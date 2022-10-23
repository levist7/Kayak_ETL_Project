import os
import logging
import scrapy
from scrapy.crawler import CrawlerProcess

"""
this spider should scrape the city names.
this script was adapted from a bootcamp class material.
"""

class oneweekin_spider(scrapy.Spider):

    # Name of your spider
    name = "citynames"

    # Url to start your spider from 
    start_urls = [
        'https://one-week-in.com/35-cities-to-visit-in-france',
    ]

    # Callback function that will be called when starting your spider
    def parse(self, response):

        quotes = [ response.xpath(f'//*[@id="main"]/article/div/div[2]/ol/li[{ind}]/a/text()') for ind in range(1,36)]
        for quote in quotes:
            yield {
                'city': quote.get(),
            }
# Name of the file where the results will be saved
filename = "../data/citylist.csv"

# If file already exists, delete it before crawling (because Scrapy will 
# concatenate the last and new results otherwise)
if filename.split('/')[-1] in os.listdir('../data/'):
        os.remove( filename)

# Declare a new CrawlerProcess with some settings
## USER_AGENT => Simulates a browser on an OS
## LOG_LEVEL => Minimal Level of Log 
## FEEDS => Where the file will be stored 
## More info on built-in settings => https://docs.scrapy.org/en/latest/topics/settings.html?highlight=settings#settings
process = CrawlerProcess(settings = {
    'USER_AGENT': 'Chrome/97.0',
    'LOG_LEVEL': logging.INFO,
    "FEEDS": {
        filename: {"format": "csv"},
    }
})

# Start the crawling using the spider you defined above
process.crawl(oneweekin_spider)
process.start()
