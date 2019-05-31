import requests
from bs4 import BeautifulSoup
import pprint

url="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
pickal_data_link=requests.get(url).text
# print pickal_data_link
url_soup=BeautifulSoup(pickal_data_link,'lxml')
total_pickles=url_soup.find('div',{'class':'_1EI9'})
pickal=total_pickles.span.get_text().split()[1]
page=int(pickal)/32+1
print page
position_no=1
for page_number in range(page):
    pickal_soup=url+"&page="+str(page_number+1)
    pickal_soup_no = requests.get(pickal_soup).text
    soup = BeautifulSoup(pickal_soup_no,'lxml')
    # print soup
    class_by=soup.find('div', {'class': '_3RA-'})
    main_class=class_by.findAll('div',{'class':'_1fje'})
    pickal_list=[]
    def pickal_detail(main_class):
        global position_no
        # print main_class
        for i in main_class:
            inside_class=i.findAll('div',{'class':'_3WhJ'})
            # position_no=0
            for j in inside_class:
                # position=position_no=position_no+1
                pickal_data={}
                # print i
                poster = j.find('div', {'class': '_3nWP'}).img['src']
                # print poster
                name = j.find('div',{'class':'_2apC'}).getText() 
                # print name
                rupees=j.find('div',{'class':'_1kMS'}).getText()
                # print rupees
                pickal_data["position"]=position_no
                pickal_data["name"] = name
                pickal_data["poster"] = poster
                pickal_data["price"] = rupees
                pickal_list.append(pickal_data)
                position_no +=1
        return pickal_list

    pprint.pprint (pickal_detail(main_class))
 