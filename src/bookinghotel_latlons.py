import os
import logging
import scrapy
from scrapy.crawler import CrawlerProcess
from datetime import date, timedelta

import pandas as pd

hotel_urllist = pd.read_csv("../data/hotellist.csv")['hotel_url'].to_list()

"""
this spider should scrape the booking hotel informations.
this script was adapted from a bootcamp class material.
"""


class booking_spider(scrapy.Spider):

    # Name of your spider
    name = "hotel_coordinates"

    # Url to start your spider from 
    start_urls = hotel_urllist

    # Callback function that will be called when starting your spider
    def parse(self, response):
        latlon = response.css("a::attr(data-atlas-latlng)").get()
        hotel_name = response.css("h2.d2fee87262.pp-header__title::text").get()
        lat, lon = latlon.split(',')	
        yield { 'hotel_name' : hotel_name,
                'lat': lat,
				'lon': lon
        }


# Name of the file where the results will be saved
filename = "../data/hotellist_latlons.csv"
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
process.crawl(booking_spider)
process.start()
