from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager


def scrape():
    # browser = init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    listings = {}

    url = "https://redplanetscience.com/"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
