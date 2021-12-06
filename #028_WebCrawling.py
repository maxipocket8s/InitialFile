import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from pandas import DataFrame

def crawl(url):
    data = requests.get(url)
    return data.content

compayniesInfo = []

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    type5 = bsObj.find("table", {"class":"type_5"})
    tltles = type5.findAll("a", {"class":"tltle"})
    hrefs = [tltle.attrs['href'] for tltle in tltles]
    for idx, href in enumerate(hrefs):
        url_ = 'https://finance.naver.com'+href
        pageString_ = crawl(url_)
        bsObj_ = BeautifulSoup(pageString_, "html.parser")
        description = bsObj_.find("div", {"class":"description"})
        category = description.find("img")['alt']
        noToday = bsObj_.find("p", {"class":"no_today"})
        blind = noToday.find("span", {"class":"blind"})
        price = blind.text
        code = bsObj_.find("span", {"class":"code"}).text
        wrapCompany = bsObj_.find("div", {"class":"wrap_company"})
        href_ = wrapCompany.find('a')
        name = href_.text
        compayniesInfo.append(name)
        compayniesInfo.append(code)
        compayniesInfo.append(price)
        compayniesInfo.append(category)
    return pd.DataFrame(np.array(compayniesInfo).reshape(-1, 4))

url = "https://finance.naver.com/sise/lastsearch2.nhn"
pageString = crawl(url)
companyInfo = parse(pageString)
print(companyInfo)
companyInfo.to_csv("C:\\Users\\pjw20\\JUWON_PY\\VSCode\\companyInfo.csv")