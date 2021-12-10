# from time import sleep
# from bs4 import BeautifulSoup as bs
# import requests


# USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15"
# LANGUAGE = "en-US,en;q=0.5"

# def create_soup(soup):
#     result = {}
#     sleep(10)
#     result['driving_time'] = soup.find("span", {"id": "drvDuration"}).text
#     return result

# def get_weather_data(url):
#     session = requests.Session()
#     sleep(10)
#     session.headers['User-Agent'] = USER_AGENT
#     session.headers['Accept-Language'] = LANGUAGE
#     session.headers['Content-Language'] = LANGUAGE
#     sleep(10)
#     html = session.get(url)
#     sleep(10)
#     # creat a soup
#     soup = bs(html.text, "html.parser")
#     # store all results on this dictionary
#     sleep(10)
#     result = create_soup(soup)
#     return result

# if __name__ == "__main__":
#     loction = "portland"
#     city = "New York"
#     # URL = "https://distancecalculator.globefeed.com/US_Distance_Result.asp?vr=apes&fromplace={location}&toplace={city}".format(location = loction, city= city)
#     URL = "https://distancecalculator.globefeed.com/US_Distance_Result.asp?vr=apes&fromplace=Portland,%20OR,%20USA&toplace=Corvallis,%20OR,%20USA"
#     # get data
#     data = get_weather_data(URL)
#     # print data
#     print("Weather for:", data["driving_time"])

from time import sleep
import urllib.request
import urllib.parse
import json

# Portland = "portland"
# Seattle = "corvallis"
url = "https://www.trippy.com/distance/{0}-to-{1}".format("Portland", "New york")
url = ''.join(url.split())
req = urllib.request.Request(url)
req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15')
response = urllib.request.urlopen(url)

# sleep(60)

html = response.read().decode('utf-8')

a = html.find('Nonstop drive: ') + 23
b = html.find('<', a)
c = b+21
d = html.find('<', c)
e = html.find('Driving time: ') + 22
f = html.find('<', e)

print(html[a:b])
print(html[c:d])
print(html[e:f])