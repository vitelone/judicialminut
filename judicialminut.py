#!/usr/bin/env python
from bs4 import BeautifulSoup
import requests, time

URL="https://www.vilaweb.cat/noticies/judici-proces-suprem-directe/"
last_tag = "unlikely text"
SECONDS=30

while True:
    data = requests.get(URL).text
    soup = BeautifulSoup(data, features="html.parser")

    tag = soup.find("div", {"class": "element-minut-a-minut"})     

    if last_tag != tag.text.encode('utf-8'):
        last_tag = tag.text.encode('utf-8')
        print last_tag

    time.sleep(SECONDS)