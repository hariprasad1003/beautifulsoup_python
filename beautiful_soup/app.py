'''
author : Hari Prasad
Resources : 
    https://www.dataquest.io/blog/web-scraping-tutorial-python/
'''

import requests
from bs4 import BeautifulSoup

page = requests.get("https://github.com/hariprasad1003")
#print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())

data = soup.find('span', class_='p-name').get_text()
#print(text)

text_file = open("scraped_data.txt", "a")
text_file.write(data)
text_file.close()

