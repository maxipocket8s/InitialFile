# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
from urllib.request import Request, urlopen
from urllib import parse
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import folium
import requests, time, json
import branca
from folium import plugins
from urllib.parse import urlencode

m = folium.Map(location=[37.566697, 126.978426],
           tiles='Stamen Terrain',
           zoom_start=11)
# tooltip = 'Click me!'
# folium.Marker([37.55510, 126.970538],
#               popup='<b>Seoul Station</b>',
#               tooltip=tooltip).add_to(m)
# folium.Marker([37.529759, 126.964642],
#               popup='<b>Yongsan Station</b>',
#               tooltip=tooltip).add_to(m)

icon_plane = plugins.BeautifyIcon(
    icon='plane',
    border_color='darkblue',
    text_color='blue',
    icon_shape='circle')
icon_flag = plugins.BeautifyIcon(
    icon='flag',
    border_color='darkred',
    text_color='red',
    icon_shape='circle')

plugins.BoatMarker(
    location=[41.584185, 161.792354],
    heading=45,
    wind_heading=120,
    wind_speed=45,
    color='purple').add_to(m)
plugins.BoatMarker(
    location=[28.572786, 157.095985],
    heading=-20,
    wind_heading=40,
    wind_speed=15,
    color='gray').add_to(m)

folium.Circle([37.566697, 126.978426],
              popup='<b>Seoul Cityhall</b>',
              radius=200,
              color='royalblue',
              fill=False).add_to(m)
folium.CircleMarker([37.5277309036199, 127.1090322252395],
                    popup='Seoul Asan Medical Center',
                    radius=20,
                    color='lightblue',
                    fill=True,
                    fill_color='blue').add_to(m)

folium.Marker([37.586928, 126.936580],
              popup="<b>Youngjune's home</b>",
              icon=folium.Icon(color='orange', icon='bookmark')).add_to(m)
folium.Marker([37.55510, 126.970538],
              popup='<b>Seoul Station</b>',
              icon=folium.Icon(color='red', icon='info-sign')).add_to(m)
folium.Marker([37.529759, 126.964642],
              popup='<b>Yongsan Station</b>',
              icon=folium.Icon(color='red', icon='info-sign')).add_to(m)
folium.Marker([37.560704, 127.038819],
              popup='<b>Wangsimni Station</b>',
              icon=folium.Icon(color='red', icon='info-sign')).add_to(m)
folium.Marker([37.558834, 126.802794],
              popup='Gimpo Airport',
              icon=icon_plane).add_to(m)
folium.Marker([37.540907, 127.079321],
              popup='Konkuk Univ.',
              icon=icon_flag).add_to(m)

# m.add_child(folium.ClickForMarker(popup='Marker'))

cities = [[37.457748575204135, 126.70222248852339],
          [36.35063814241654, 127.38481869822748],
          [35.1602870917421, 126.85138996751687],
          [35.87707307641006, 128.6011535814839],
          [35.550317204257524, 129.30968582343553],
          [35.17995922925898, 129.0749461318313]]
for i in range(len(cities)):
    folium.Circle(
        location=cities[i],
        radius=200,
        color='red',
        ).add_to(m)
    
folium.PolyLine(
    locations=cities,
    tooltip='Trip Route',
    color='orange').add_to(m)
folium.Rectangle(
    bounds=cities,
    tooltip='Trip Bound').add_to(m)
# folium.Polygon(
#     locations=cities,
#     fill=True,
#     tooltip='Polygon').add_to(m)

wind_positions=[[33.28635221261911, 131.53421345964858],
               [33.87643540417761, 129.70665738582701],
               [34.84023734562776, 127.89214724308928],
               [36.082415342576454, 126.68973049804505],
               [37.442462819220864, 122.12365303377956],
               [37.885656265158346, 118.51556957405698]]
wind_line=folium.PolyLine(
    wind_positions,
    weight=15,
    color='deepskyblue').add_to(m)
plugins.PolyLineTextPath(
    wind_line,
    ') ',
    repeat=True,
    offset=10,
    attributes={'fill': 'dodgerblue', 'font-weight': 'bold', 'font-size': 24}).add_to(m)

m.save('SeoulMap.html')



data = pd.read_csv('C:\\Users\\pjw20\\Coding\\Spyder\\BigdataCampus\\data1.csv', encoding='CP949')

# client_id = "lgmzq1x90e"
# client_pw = "DP29vvANgVeQgZCbLbBf07zWnWi6rBjipg3hUkBR"
# def get_gps_naver(address):
#     api_url = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode"
#     geo_coordi = []
#     for address in data['시설주소']:
#         # print(address)
#         add_url = parse.quote(address)
#         # print(add_url)
#         url = api_url + add_url
#         # print(url)
#         reqt = Request(url)
#         reqt.add_header('X-NCP-APIGW-API-KEY-ID', client_id)
#         reqt.add_header('X-NCP-APIGW-API-KEY', client_pw)
#         try:
#             response = urlopen(reqt)
#         except HTTPError as e:
#             print("HTTP Error!")
#             latitude = None
#             longitude = None
#         else:
#             rescode = response.getcode() # 정상이면 200 리턴
#             if rescode == 200:
#                 response_body = response.read().decode('utf-8')
#                 response_body = json.loads(response_body)
#                 if 'addresses' in response_body:
#                     latitude = response_body['addresses'][0]['y']
#                     longitude = response_body['addresses'][0]['x']
#                     print('Success!')
#                 else:
#                     print('Result not exist!')
#                     latitude = None
#                     longitude = None
#             else:
#                 print("Response error code: %d" % rescode)
#         geo_coordi.append([latitude, longitude])
                
# get_gps_naver(data)

def getJson(url, params={}, wait=5, headers={}):
    print(url + ('?' + urlencode(params) if len(params) > 0 else ''))
    while True:
        r = requests.get(url, params=params, headers=headers)
        if len(r.text.strip()) == 0:
            time.sleep(3)
        else:
            break
    js = json.loads(r.text)
    time.sleep(wait)
    return js

def get_gps_naver(address):
    url = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode"
    headers = {
        "X-NCP-APIGW-API-KEY-ID": "lgmzq1x90e",
        "X-NCP-APIGW-API-KEY": "DP29vvANgVeQgZCbLbBf07zWnWi6rBjipg3hUkBR"}
    road, jibun, lat, lng = "","",0,0
    if address:
        params = { "query": address }
        js = {}
        while True:
            js = getJson(url, params, 0, headers)
            if "meta" not in js:
                time.sleep(10)
            else:
                break
        if js["meta"]["totalCount"] > 0:
            road = js["addresses"][0]["roadAddress"]
            jibun = js["addresses"][0]["jibunAddress"]
            lat = float(js["addresses"][0]["y"])
            lng = float(js["addresses"][0]["x"])
    return lat, lng

geo_info = []
for address in data['시설주소']:
    print(address)
    geo_info.append(get_gps_naver(address))
    
print(geo_info)