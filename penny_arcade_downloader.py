
import requests
from bs4 import BeautifulSoup
import os
import urllib.request


#//Penny Arcade Comic Scraper


os.chdir('I:\\Scrape')

url = 'https://www.penny-arcade.com/comic/'

def pa_urlDate():

    #//generate the 2018/xx/xx format to add to the end of the url


    month = list(range (1,13))

    day = list(range(0,32))

    ret_lst = []



    for i in range(len(month)):

        if month[i] < 10:


            for d in day:


                if day[d] < 10:

                    ret_lst.append (url + '2017/0{}/0{}'.format (month[i],day[d]))

                else:
                    ret_lst.append (url + '2017/0{}/{}'.format (month[i],day[d]))

        else:

            for d in day:

                if day[d] <10:

                    ret_lst.append (url + '2017/{}/0{}'.format(month[i], day[d]))

                else:

                    ret_lst.append (url + '2017/{}/{}'.format(month[i], day[d]))

    return ret_lst


url_list = pa_urlDate()  #// iterate this for the url end dates

for i in range(len(url_list)):

    r = requests.get(url_list[i])

    pa_soup = BeautifulSoup(r.text, 'html.parser')

    check404 = pa_soup.find_all('h2')



    if check404[0].text == '404':

        continue

    else:

        imgLoc = pa_soup.find_all('img')[0]['src']

        urllib.request.urlretrieve(imgLoc, 'pa{}.jpg'.format(str(i)))