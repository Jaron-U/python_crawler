from bs4 import BeautifulSoup as bs
import requests

def get_name_rating(item, result, soup, i):
    result['name'] = item.find('h4').get_text()
    result['reviewCount'] = soup.select('[class*=reviewCount]')[i+2].get_text()
    result['rating'] = soup.select('[aria-label*=rating]')[i+2]['aria-label']
    result['priceRange'] = soup.select('[class*=priceRange]')[i].get_text()


def get_type(all_p, result):
    temp = all_p
    type_r = 'css-1p8aobs'
    types = ''
    while type_r in temp:
        a = temp.find('css-1p8aobs')+13
        b = temp.find('<', a)
        types += "|"
        types += temp[a:b] + "|\t"
        temp = temp[b:]
    result['type'] = types

def get_position(all_p, result):
    a = all_p.find("css-1e4fdj9") + 13
    b = all_p.find("<", a)
    result['position'] = all_p[a:b]

def get_link(item):
    link = item.find('h4')
    link = str(link)
    u_link = "https://www.yelp.com/"
    a = link.find('href=\"')+6
    b = link.find('\"', a)
    result['link'] = u_link+link[a:b]


headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15'}
url='https://www.yelp.com/search?cflt=restaurants&find_loc=' + 'San Francisco'
response=requests.get(url,headers=headers)
soup=bs(response.content,'lxml')
restaustants = soup.select('[class*=container]')[16:24]
i=0; t_result={}
for item in restaustants:
    if item.find('h4'):
        result = {}
        get_name_rating(item, result, soup, i)
        all_p = item.find("p")
        all_p = str(all_p)
        get_type(all_p,result)
        get_position(all_p, result)
        get_link(item)
        t_result[i] = result
        i+=1
       

for j in t_result:
    print(t_result[j]['name'])
    print(t_result[j]['priceRange'])
    print(t_result[j]['type'])
    print(t_result[j]['link'])
    print(t_result[j]['reviewCount'])
    print(t_result[j]['rating'])
    print("-----------------")



###viewspots
# from bs4 import BeautifulSoup as bs
# import requests


# def get_name_rating(item, result, soup):
#     result['name'] = item.find('h4').get_text()
#     result['reviewCount'] = soup.select('[class*=reviewCount]')[0].get_text()
#     print(result['reviewCount'])
#     result['rating'] = soup.select('[aria-label*=rating]')[0]['aria-label']

# def get_type_position(item, result):
#     name = item.find("p")
#     name = str(name)
#     a = name.find("css-1p8aobs")+13
#     b = name.find('<', a)
#     result['type'] = name[a:b]
#     c = name.find("css-1e4fdj9")+13
#     d = name.find('<', c)
#     result['position'] = name[c:d]

# def get_link(item, result):
#     u_link = "https://www.yelp.com/"
#     link = item.find("a")
#     link = str(link)
#     a = link.find("css-1lwccx4") + 20
#     b = link.find("\"", a)
#     result['link'] = u_link+link[a:b]


# headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15'}
# url = 'https://www.yelp.com/search?find_desc=scenic+spots&find_loc=New+York'
# response=requests.get(url,headers=headers)
# soup=bs(response.content,'lxml')
# restaustants = soup.select('[class*=container]')[10:18]
# for item in restaustants:
#     if item.find('h4'):
#         result = {}
#         get_name_rating(item, result, soup)
#         get_type_position(item, result)
#         get_link(item, result)
#         print(result['name'])
#         print(result['type'])
#         print(result['link'])
#         print(result['rating'])
#         print('------------------')
