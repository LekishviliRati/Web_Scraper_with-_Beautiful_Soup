from bs4 import BeautifulSoup
import requests

source = requests.get("https://koesio-project.herokuapp.com/").text

soup = BeautifulSoup(source, 'lxml')

print(soup.prettify())
