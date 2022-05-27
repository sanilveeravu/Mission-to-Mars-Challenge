# Import Splinter, BeautifulSoup, and Pandas

from splinter import Browser
from bs4 import BeautifulSoup as soup 
from webdriver_manager.chrome import ChromeDriverManager
import datetime as dt
import time

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

def scrape_all():

    # Set up Splinter
    executable_path = {'executable_path':ChromeDriverManager().install()}
    browser = Browser('chrome',**executable_path,headless=True)
    news_title, news_paragraph = mars_news(browser)
    hemisphere_image_urls = mars_hemispheres(browser)

    # Run all scraping functions and store results in dictionary
    data = {
      "news_title": news_title,
      "news_paragraph": news_paragraph,
      "featured_image": featured_image(browser),
      "facts": mars_facts(),
      "hemispheres": hemisphere_image_urls,
      "last_modified": dt.datetime.now()
    }

    # Stop webdriver and return data
    browser.quit()
    return data

def mars_news(browser):

    # Visit the mars nasa news site
    url = 'https://redplanetscience.com'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text',wait_time=1)

    html = browser.html 
    news_soup = soup(html, 'html.parser')

    # Add try/except for error handling

    try:

        slide_elem = news_soup.select_one('div.list_text')

        slide_elem.find('div', class_='content_title')

        news_title = slide_elem.find('div',class_='content_title').get_text()
        news_title

        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div',class_='article_teaser_body').get_text()
        news_p

    except AttributeError:
        return None, None     

    return news_title, news_p

def featured_image(browser):

    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    try:

        # Find the relative image url
        img_url_rel = img_soup.find('img',class_='fancybox-image').get('src')
        img_url_rel

    except AttributeError:
        return None    

    # Use the base URL to create an absolute URL
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'
    
    return img_url



# ## Mars Facts
def mars_facts():
    try:

        # use 'read_html" to scrape the facts table into a dataframe
        df = pd.read_html('https://galaxyfacts-mars.com',header=0)[0]
        df.head() 
    except BaseException:
        return None
    #Improvements on table data from module to avoid repeated titles as the table extracted already had headers
    #df.columns=['description', 'Mars', 'Earth']
    #df.set_index('description',inplace=True)
        
    # Convert dataframe into HTML format, add bootstrap
    return df.to_html(classes="table table-striped",index=False)

def mars_hemispheres(browser):
    url = 'https://marshemispheres.com/'
    browser.visit(url)

    # 2. Create a list to hold the images and titles.
    hemisphere_image_urls = []

    # 3. Write code to retrieve the image urls and titles for each hemisphere.
    # Parse the resulting html with soup
    html = browser.html
    hemi_soup = soup(html, 'html.parser')

    hemisphere_full_urls = []

    hemisphere_list = hemi_soup.find_all('div',class_='description')
    for hemisphere in hemisphere_list:
        hemisphere_title=hemisphere.find('h3').get_text()
        hemisphere_url=hemisphere.find('a').get('href')
        browser.links.find_by_partial_href(hemisphere_url)[1].click()
        time.sleep(2)
        subpage_html = browser.html
        hemi_sub_soup = soup(subpage_html, 'html.parser')
        full_image_url = url+hemi_sub_soup.find('a',text="Sample").get('href')
        hemisphere_image_urls.append({"img_url":full_image_url,"title":hemisphere_title})
        browser.back()
        time.sleep(2)

    # 4. Print the list that holds the dictionary of each image url and title.
    return hemisphere_image_urls

    # 5. Quit the browser

if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_all())
