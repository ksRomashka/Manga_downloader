import time
from selenium import webdriver
import json

def authorization(url):
    driver = webdriver.Edge()
    driver.get(url)

    time.sleep(30)

    cookies = driver.get_cookies()
    with open('cookies.json', 'w') as file:
        json.dump(cookies, file)

    driver.close()

if __name__ == "__main__":
    print("https://mangalib.me/ru/manga/6950--banana-fish")
    url = input()
    authorization(url)