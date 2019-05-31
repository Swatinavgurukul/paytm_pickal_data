import requests
from bs4 import BeautifulSoup
import pprint

pickal_data_link=requests.get("https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471").text
# print pickal_data_link
soup=BeautifulSoup(pickal_data_link,'lxml')
# print soup

def pickal_detail(soup):

    pickal_data={}
    poster = soup.find('div', {'class': '_3nWP'}).img['src']
    # print poster
    name = soup.find('div',{'class':'_2apC'}).getText() 
    # print name
    rupees=soup.find('div',{'class':'_1kMS'}).getText()
    # print rupees
    pickal_data["name"] = name
    pickal_data["poster"] = poster
    pickal_data["price"] = rupees

    return pickal_data
print (pickal_detail(soup))