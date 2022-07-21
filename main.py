from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
from Scweet.scweet import scrape
from Scweet.user import get_user_information, get_users_following, get_users_followers
import time
from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs
import re
import json

global totalrequests
totalrequests = 0


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
}

def getreddit():
    global totalrequests
    page = requests.get("https://www.reddit.com/r/redditdev/", headers=headers)
    soup = BeautifulSoup(page.text, "lxml")
    title = soup.find('div', class_="_3b9utyKN3e_kzVZ5ngPqAu").text
    totalrequests = totalrequests + 1
    return title

def getfacebook():
    global totalrequests
    page = requests.get("https://www.facebook.com/Google/about/", headers=headers)
    soup = BeautifulSoup(page.text, "lxml")
    title = soup.find('span', class_="d2edcug0 hpfvmrgz qv66sw1b c1et5uql oi732d6d ik7dh3pa ht8s03o8 jq4qci2q a3bd9o3v b1v8xokw oo9gr5id").text
    totalrequests = totalrequests + 1
    return title

def gettwitter():
    global totalrequests
    page = requests.get("https://twitter.com/Google", headers=headers)
    soup = BeautifulSoup(page.text, "lxml")
    title = soup.find('span', class_="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0").text
    totalrequests = totalrequests + 1
    print(title)



print(getreddit())
