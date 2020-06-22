from bs4 import BeautifulSoup
import params
import DB
import time
import random
from selenium import webdriver
from lxml import etree

provinceUrls = params.provinceUrls
proxies = params.proxies
headers = params.anjukeHeaders
cookies = params.anjukeCookies


def getAllProvinceCityPrice():
    for url in provinceUrls:
        print(url)
        getProvinceContent(url)
        time.sleep(random.randint(1, 3))


def getProvinceContent(url):
    driver = webdriver.Chrome()

    driver.get(url)

    page = etree.HTML(driver.page_source)
    html = etree.tostring(page, encoding=str, pretty_print=True)

    soup = BeautifulSoup(html, 'lxml')

    names = soup.select('.fjlist-box > ul > li > a > b')
    prices = soup.select('.fjlist-box > ul > li > a > span')
    for i, name in enumerate(names):
        name = str(name).split('房')[0]
        name = str(name).split('年')[1]

        price = prices[i]
        price = str(price).split('<span>')[1]
        price = str(price).split('元')[0]

        print(name)
        print(price)
        DB.insertCityHousePrice(name, price)


if __name__=='__main__':
    getAllProvinceCityPrice()
    # getProvinceContent('')
