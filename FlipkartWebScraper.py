import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url= "https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy,4io&otracker=nmenu_sub_Electronics_0_Mi"
uClient = uReq(my_url)
page_html = uClient.read()

uClient.close()
page_soup= soup(page_html, "html.parser")
file = open("DataBase.txt", "w", encoding="utf-8")
file.write('Flipkart Data')
containers= page_soup.findAll("div",{"class":"col _2-gKeQ"})

name= page_soup.findAll("div",{"class":"_3wU53n"})
ram= page_soup.findAll("div",{"class":"OiPjke"})
rating= page_soup.findAll("div",{"class":"niH0FQ"})
disc= page_soup.findAll("div",{"class":"_3ULzGw"})

for i in range(0,len(name)):
    print('Name :'+ name[i].text)
    file.write('Name :'+ name[i].text)
    print('RAM :'+ ram[i].text)
    file.write('RAM :'+ ram[i].text)
    x= rating[i].text.split(" ")
    print('Stars :'+ x[0])
    file.write('Stars :'+ x[0])
    print('Rated By :'+ x[1]+ 'people')
    file.write('Rated By :'+ x[1]+ 'people')
    print('Discription :'+ disc[i].text)
    file.write('Discription :'+ disc[i].text)
    print('\n')
    file.write('\n')
    
    
    
