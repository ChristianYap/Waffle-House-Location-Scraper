#################################################################################
# Name: Christian Yap
# Description: Get Waffle House Locations from website
# Version: 1.0, Created March 2020
# Requirements: Python vs 3.7 or above
# Command to run in terminal under the same directory: scrapy crawl scrollWaffle -L WARN
#################################################################################
# These "imports" are external libraries that we need to use to scrape data from a website.
# They are usually installed on top of Python being installed.
import csv
import json
import scrapy


# Let's start the web crawler, nicknamed spiders...
class Spider1(scrapy.Spider):

    # name of our spider, also known as our web data scraper:
    name = "scrollWaffle"

    # link to where we are going to get our Waffle House Locations
    # Getting the links is a bit tricky, you need to use Google Chrome and see how it is asking the Waffle House Website for the info
    # I can show you sometime!
    api_url = ['https://locations.wafflehouse.com/api/587d236eeb89fb17504336db/locations-details?locale=en_US']
    start_urls = ['https://locations.wafflehouse.com/api/587d236eeb89fb17504336db/locations-details?locale=en_US']

    # At this point, when we run this program, we should have the data from the URL above
    def parse(self, response):
        # Let's load the ALL the data we have gotten from the waffle house website into a variable, call it "data":
        data = json.loads(response.text)
        header = True                       # This is just so we input the category names (such as branch, address, etc) once.
        # Let's create a .csv file to save all that data
        with open('WaffleHouseLocations.csv', 'w', newline='') as f:
            # Let's parse through the data we got from the website first
            # To do so, you have to know how they are storing the data, can show this sometime too!
            for wafflehouse in data['features']:
                coord = wafflehouse['geometry']['coordinates']
                results = ' '.join([str(item) for item in coord])
                coordinates = results.split(' ')
                # Let's only save the specific data we want:
                yield
                var = {
                    'branch': wafflehouse['properties']['branch'],
                    'address': wafflehouse['properties']['addressLine1'],
                    'city': wafflehouse['properties']['city'],
                    'state': wafflehouse['properties']['province'],
                    'country': wafflehouse['properties']['country'],
                    'longitude': coordinates[0],
                    'latitude': coordinates[1]
                }

                # We insert a new waffle house branch and related info to it to our .csv file
                if header:
                    w = csv.DictWriter(f, var.keys())
                    w.writeheader()
                    header = False
                w.writerow(var)

        # Now that all the information is in the .csv, let's separate the coordinates into x,y:




        # Close the writer that allows us to write the .csv file
        f.close()
    # Done, now we geocode!

