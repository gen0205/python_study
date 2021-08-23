# -*- coding: utf-8 -*-
import sys
import urllib.request
from bs4 import BeautifulSoup

def main():
    url = getArgument()
    if url is None:
        return False
    with urllib.request.urlopen(url) as response:
        html = response.read().decode("utf8")
    # print(html)
    soup = BeautifulSoup(html, features="html.parser")
    for link in soup.find_all('a'):
        print(link.get('href'))
    return True

def getArgument():
    params = sys.argv
    length = len(params)
    if length == 2:
        return params[1]
    print("Cannnot get argument...")
    return None

if __name__ == "__main__":
    if main():
        print("================")
        print("Success!")
        print("================")
    else:
        print("error occured!")
