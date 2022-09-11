from requests import get
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs

options = Options()
browser = webdriver.Chrome(options=options)

def get_page_count(keyword):
  base_url = 'https://kr.indeed.com/jobs?q='
  browser.get(f"{base_url}{keyword}&limit=50")
  soup = BeautifulSoup(browser.page_source, "html.parser")
  pagination = soup.find("ul",class_="pagination-list")
  if pagination == None:
    return 1 
  pages = pagination.find_all("li", recursive=False)
  count = len(pages)
  if count >= 5:
    return 5
  else:
    return count

print(get_page_count("java"))
print(get_page_count("django"))
print(get_page_count("nest"))
print(get_page_count("react"))
print(get_page_count("c#"))
print(get_page_count("python"))

def extract_indded_jobs(keyword):
  base_url = 'https://kr.indeed.com/jobs?q='
  browser.get(f"{base_url}{keyword}")

  results=[]
  soup = BeautifulSoup(browser.page_source, "html.parser")
  job_list = soup.find("ul", class_="jobsearch-ResultsList")
  jobs = job_list.find_all("li", recursive=False)
  for job in jobs :
    zone = job.find("div", class_="mosaic-zone")
    if zone == None: 
      anchor = job.select_one("h2 a")
      title = anchor['aria-label']
      link = anchor['href']
      company = job.find("span", class_="companyName")
      location = job.find("div", class_="companyLocation")
      job_data = {
        'link': f"https://kr.indeed.com{link}",
        'company': company.string,
        'location': location.string,
        'position': title
      }
      results.append(job_data)
  for result in results:
    print(result,"\n//////\n")
  
