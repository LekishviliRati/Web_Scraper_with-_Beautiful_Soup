from bs4 import BeautifulSoup
import requests

source = requests.get("https://koesio-project.herokuapp.com/").text

soup = BeautifulSoup(source, 'lxml')

article = soup.find('article')

headline = article.h1.text

print(headline)
