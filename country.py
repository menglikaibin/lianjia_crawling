from bs4 import BeautifulSoup
import lxml
import requests
import params
import generateProxy

provinceUrls = params.provinceUrls
proxies = params.proxies
headers = params.anjukeHeaders
cookies = params.anjukeCookies


def getAllCityUrl():
    for url in provinceUrls:

        html = requests.get(url).content
        soup = BeautifulSoup(html, 'lxml')


def getProvinceContent(url):
    url = 'http://www.anjuke.com/fangjia/neimenggu/'
    proxies = generateProxy.generate()

    with requests.Session() as sess:
        html = sess.get(url, headers=headers, cookies=cookies, proxies=proxies)

        soup = BeautifulSoup(html.content, 'lxml')
        print(soup)


getProvinceContent('')
