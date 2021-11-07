# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()

options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu-sandbox')
options.add_argument("--single-process")
options.add_argument('window-size=1920x1080')
options.add_argument(
    '"user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"')

options.binary_location = "/bin/headless-chromium"
driver = webdriver.Chrome(
    executable_path="/bin/chromedriver", options=options)


def get_notice(url):

    driver.get(url)
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    html = soup.find("table", {"class": "artclTable artclHorNum1"})
    
    notice_headline = html.find('tbody').find_all("tr")
    
    notices = []
    
    for notice in notice_headline:
        n = notice.find('td', {'class': '_artclTdTitle'}).find('a')
        title = n.find('strong').string
        link = n.get('href')
        notices.append({'title': title, 'link': link})
        
    driver.quit()
    
    return notices