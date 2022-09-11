from requests import get
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs

options = Options()
browser = webdriver.Chrome(options=options)

base_url = 'https://kr.indeed.com/jobs?q='
keyword = 'python'

browser.get(f"{base_url}{keyword}&limit=50")

soup = BeautifulSoup(browser.page_source, "html.parser")
job_list = soup.find("ul", class_="jobsearch-ResultsList")
jobs = job_list.find_all("li", recursive=False)
for job in jobs :
  zone = job.find("div", class_="mosaic-zone")
  if zone == None: 
    anchor = job.select_one("h2 a")
    title = anchor['aria-label']
    link = anchor['href']