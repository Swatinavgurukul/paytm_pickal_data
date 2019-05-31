import requests
from bs4 import BeautifulSoup
import pprint

pickal_data_link=requests.get("https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471").text
# print pickal_data_link
soup=BeautifulSoup(pickal_data_link,'lxml')
# print soup
class_by=soup.find('div', {'class': '_3RA-'})
main_class=class_by.findAll('div',{'class':'_1fje'})
pickal_list=[]
def pickal_detail(main_class):
    # print main_class
    for i in main_class:
        inside_class=i.findAll('div',{'class':'_3WhJ'})
        for j in inside_class:

            pickal_data={}
            # print i
            poster = j.find('div', {'class': '_3nWP'}).img['src']
            # print poster
            name = j.find('div',{'class':'_2apC'}).getText() 
            # print name
            rupees=j.find('div',{'class':'_1kMS'}).getText()
            # print rupees
            pickal_data["name"] = name
            pickal_data["poster"] = poster
            pickal_data["price"] = rupees
            pickal_list.append(pickal_data)
    return pickal_list
pprint.pprint (pickal_detail(main_class))