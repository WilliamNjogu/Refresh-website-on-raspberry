import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import configparser


def options():
    chrome_options = Options()
    return chrome_options


def refresh_website(urls, refresh_interval):
    driver = webdriver.Chrome(options=options())
    driver.set_window_position(0, 0)

    driver.get(urls[0])

    while True:
        for url in urls[1:]:
            driver.execute_script(f"window.location.href = '{url}'")
            time.sleep(refresh_interval)


config = configparser.ConfigParser()
config.read('config.ini')

refresh_interval = int(config.get('Settings', 'refresh_interval'))
urls = config.get('Settings', 'urls').split()

refresh_website(urls, refresh_interval)
