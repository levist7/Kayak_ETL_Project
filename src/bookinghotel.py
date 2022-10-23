import os
import logging
import scrapy
from scrapy.crawler import CrawlerProcess
from datetime import date, timedelta

import pandas as pd
import json
#searching for 2 nights stay, 4 days from today
checkin = date.today() + timedelta(days=4) 
checkout = date.today()  + timedelta(days=6)

#checkin and checkout dates
dayin, monthin, yearin = checkin.day  ,checkin.month, checkin.year
dayout, monthout, yearout = checkout.day ,checkout.month, checkout.year

city_list = pd.read_csv("../data/top5city.csv")['city'].to_list()

"""
this spider should scrape the booking hotel informations.
this script was adapted from a bootcamp class material.
"""


class booking_spider(scrapy.Spider):

    # Name of your spider
    name = "hotels"

    # Url to start your spider from 
    start_urls = [
        'https://www.booking.com/searchresults.html?',
    ]

    # Callback function that will be called when starting your spider
    def parse(self, response):
        print('\n\nsearch\n\n')  
        print(response.url,'\n\n')      
        for ii in range(len(city_list)):
            print('\n\n\n City Name: ',city_list[ii],'\n\n\n')
            book_info = {
                'ss':city_list[ii],
                'checkin_year':str(yearin),'checkin_month':str(monthin),'checkin_monthday':str(dayin),
                'checkout_year':str(yearout),'checkout_month':str(monthout),'checkout_monthday':str(dayout),
                #'offset': '0'
                'order':'class'
            }
            out=  scrapy.FormRequest.from_response(response, 
                    formdata = book_info, 
                    callback = self.after_search)
            print('\n\n\nOUT= ',out,'\n\n\n')
            yield out

    # Callback used after login

    def after_search(self, response):
        
        results = response.css('div.b978843432')
        
        print('\n\n\naftersearch\n\n\n')
        print('results = ', results,'\n\n\n')

        for hotel in results:
            out = {'hotel_city': hotel.xpath("/html/body/div[3]/div/div[3]/div[1]/div[1]/div[1]/div/div/div/h1/text()").get().split(":")[0],
				   'hotel_name': hotel.css("div.fcab3ed991.a23c043802::text").get(),
				   'hotel_score' : hotel.css("div.b5cd09854e.d10a6220b4::text").get(),
				   'hotel_desc': hotel.css("span.df597226dd::text").get(),
				   'hotel_url' : hotel.css('a::attr(href)').get().split('?')[0],
				   }
            yield out

# Name of the file where the results will be saved
filename = "../data/hotellist.csv"
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
