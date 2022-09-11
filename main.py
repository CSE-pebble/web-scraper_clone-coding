from requests import get
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs

options = Options()
browser = webdriver.Chrome(options=options)

base_url = 'https://kr.indeed.com/jobs?q='
keyword = 'python'

browser.get(f"{base_url}{keyword}")

soup = BeautifulSoup(browser.page_source, "html.parser")
