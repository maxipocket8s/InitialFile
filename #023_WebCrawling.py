import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from pandas import DataFrame

# Crawl >> Parse 데이터 가져와서 정보 뽑아내기
real_h2_list = []
real_address_list = []
real_dd_list = []
for i in range(1, 76):
    url = "https://www.hadong.go.kr/02642/02655/03526.web?&cpage={}".format(i)
    req = requests.get(url)
    bsObj = BeautifulSoup(req.content, 'html.parser')
    texts = bsObj.findAll('div', {'class':'texts'})
    hrefs = [div.find('a')['href'] for div in texts]
    for j in range(len(hrefs)):
        url = "https://www.hadong.go.kr/02642/02655/03526.web" + hrefs[j]
        req = requests.get(url)
        bsObj = BeautifulSoup(req.content, 'html.parser')
        spc4hg1food1view1 = bsObj.find('div', {'class' : 'spc4hg1 food1view1'})
        h2 = spc4hg1food1view1.find('h2', {'class' : 'h1'})
        real_h2 = h2.get_text()
        address = bsObj.find('p', {"class" : "address"})
        real_address = address.get_text()
        even = bsObj.find('div', {'class' : 'even-grid diffmix-2 float-left vgap00 food1view1'})
        md = even.find('div', {'class' : 'md-42pct column'})
        wrap1 = md.find('div', {'class' : 'wrap1'})
        spc4view1 = wrap1.find('div', {'class' : 'spc4view1 type2'})
        spc4info2 = spc4view1.find('div', {'class' : 'spc4info2'})
        dl1 = spc4info2.find('ul', {'class' : 'dl1 mgtb0'})
        di = dl1.find('li', {'class' : 'di phone'})
        w1 = di.find('div', {'class' : 'w1'})
        dd = w1.find('span', {'class' : 'dd'})
        real_dd = dd.get_text()
        real_h2_list.append(real_h2)
        real_address_list.append(real_address)
        real_dd_list.append(real_dd)

arr_h2 = np.array(real_h2_list).reshape(1, len(real_h2_list))
arr_address = np.array(real_address_list).reshape(1, len(real_address_list))
arr_dd = np.array(real_dd_list).reshape(1, len(real_dd_list))
Hadong = np.concatenate([arr_h2, arr_address, arr_dd], axis=0)
real_Hadong = np.transpose(Hadong)
print(real_Hadong.shape)
df = pd.DataFrame(real_Hadong)
df.to_csv('C:\\Users\\pjw20\\JUWON_PY\\VSCode\\Hadong.csv', header = ['업소명', '주소', '연락처'], encoding = 'euc-kr')