import bs4
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from feedgen.feed import FeedGenerator
import datetime
import pytz

import requests

def process_page(page_source):
    soup        = bs4.BeautifulSoup(page_source, 'html.parser')

    for entry in soup.find_all('article'):
        fe = fg.add_entry()

        # General information about the episode
        eaudio = entry.find('div', {'class': 'sqs-audio-embed'})
        fe.id(eaudio['data-title'])
        fe.title(eaudio['data-title'])

        # create the resource link
        url   = eaudio['data-url']
        size  = requests.head(url).headers['Content-Length']
        fe.enclosure(url, size, 'audio/mpeg')

        # episode length
        timedelta = datetime.timedelta(milliseconds=int(eaudio['data-duration-in-ms']))
        fe.podcast.itunes_duration(timedelta)

        # episode description is in the first paragraph tag
        desc   = entry.find('p')
        fe.summary(desc.text)

        # Get the publication time info
        etime  = entry.find('time', {'class': 'published'})
        d = datetime.datetime.strptime(etime['datetime'], '%Y-%m-%d')
        d = d.replace(tzinfo = pytz.timezone('UTC'))
        fe.published(d)

# Create the FeedGenerator object
fg = FeedGenerator()
fg.load_extension('podcast')
fg.podcast.itunes_category('Science & Medicine','Natural Sciences')
fg.id('https://www.indefenseofplants.com/podcast')
fg.title('In Defense Of Plants')
fg.description('It would seem that most people don’t pay any attention to plants unless they are pretty or useful in some way. I reject this reality outright. Plants are everything on this planet. They have this amazing ability to use our nearest star to break apart water and CO2 gas in order to grow and reproduce. From the smallest duckweed to the tallest redwood, the botanical world is full of amazing evolutionary stories. I am here to tell those stories. My name is Matt and I am obsessed with the botanical world. In Defense of Plants is my way of sharing that love with you. ')
fg.author({'name': 'Matt Candeias', 'email':'matt@indefenseofplants.com'})
fg.link(href='https://www.indefenseofplants.com/podcast')
fg.logo('https://images.squarespace-cdn.com/content/v1/544591e6e4b0135285aeb5b6/1512588666285-UBKCIK0UFIBDHV2ZFKBU/ke17ZwdGBToddI8pDm48kEnKpXrmwkJNOlSTKwNL29RZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZamWLI2zvYWH8K3-s_4yszcp2ryTI0HqTOaaUohrI8PIh4iASq-5YOPh5eoH282P5lK1nuApnfj5Amkpayu2HR4/image-asset.png?format=256w')
fg.language('en')

# Initalize Selenium
binary = r'C:\Program Files\Mozilla Firefox\firefox.exe'
options = Options()
options.headless = True
options.binary = binary
cap = DesiredCapabilities().FIREFOX
cap["marionette"] = True #optional
driver = webdriver.Firefox(options=options, capabilities=cap, executable_path="geckodriver.exe")

# Render Page
url = 'https://www.indefenseofplants.com/podcast'
driver.get(url)

# Process the return of the first page
process_page(driver.page_source)

# While we have an "older-posts" link, keep clicking the link and processing
# the new page
while driver.find_elements_by_class_name('older-posts'):
    driver.find_element_by_class_name('older-posts').click()
    process_page(driver.page_source)

fg.rss_file('idop.xml')
