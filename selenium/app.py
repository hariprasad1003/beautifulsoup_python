import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import pandas as pd

browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=webdriver.ChromeOptions())

browser.get('https://github.com/hariprasad1003')

timeout = 60

try:
    WebDriverWait(browser, timeout)
except TimeoutException:
    browser.quit()

repo_name = browser.find_elements_by_xpath("//span[@class='repo']")

output_array = []
for element in repo_name:
    output = element.text
    output_array.append(output)
    print(output)


df = pd.DataFrame(list(zip(output_array)), columns=['Repositories'])

repo_data = df.to_csv('repo.csv', index=False)
