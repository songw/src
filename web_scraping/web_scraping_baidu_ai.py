import requests
from bs4 import BeautifulSoup
import time
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
    'Cookie': '_vwo_uuid_v2=D0BD1439EB2B1C0EE5C9B996CE5A85416|a816731533a7d092c9ea4614415fb471; gr_user_id=0ad7a52a-2c13-4a80-ae60-41c001559fb0; douban-fav-remind=1; bid=PbJTAn0We4Q; viewed="27108685_26278021_30237842_35188914_5377669_30352656_2856039_5252170_1313142_27593453"; ll="118183"; push_noty_num=0; push_doumail_num=0; __utmv=30149280.5959; __utma=30149280.1159876898.1573719787.1621503273.1621842000.29; __utmc=30149280; __utmz=30149280.1621842000.29.6.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1621931326%2C%22https%3A%2F%2Fwww.google.com.hk%2F%22%5D; _pk_ses.100001.8cb4=*; dbcl2="59599558:NMGtTCxaX1Y"; ck=FXN5; _pk_id.100001.8cb4=390c93defd5467ff.1581564560.25.1621931341.1621841998.; ap_v=0,6.0'
}


response = requests.get(
    'https://ai.baidu.com/productlist#tech', headers=headers)

abilities = []

soup = BeautifulSoup(response.text, 'lxml')
ai_productlist_content_sections = soup.find_all(
    'div', {'class': 'ai-productlist-content-section'})
for childproduct in ai_productlist_content_sections[0].find_all('div', {'class': 'ai-productlist-content-item-childProduct'}):
    for test in childproduct(
            'a', {'class': 'ai-productlist-content-item-childProduct-title'}):
        abilities.append(test.get_text().strip())

with open('baidu.csv', 'w') as file:
    writer = csv.writer(file, delimiter=',')

    writer.writerow(["能力"])

    for i in range(len(abilities)):
        writer.writerow([
            abilities[i]
        ])
