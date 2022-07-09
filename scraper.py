from bs4 import BeautifulSoup
import requests
import csv

source = requests.get("https://koesio-project.herokuapp.com/").text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('scraper.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['title', 'link'])

article = soup.find('article')

# print(article.prettify())

# # Get H1 title from home page
# headline = article.h1.text
#
# print(headline)

# Get links with title from home page save them in a CSV file
for link in article.find_all('a'):
    link_href = link.get('href')
    # print(href_link)
    link_title = link.text
    csv_writer.writerow([link_title, link_href])


csv_file.close()
