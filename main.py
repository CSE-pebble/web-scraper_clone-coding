from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
search_term = "python"

response = get(f"{base_url}{search_term}")
if response.status_code != 200:
  print("Can't request website")
else:
  soup = BeautifulSoup(response.text, "html.parser") # HTML 다 가져옴
  jobs = soup.find_all("section", class_="jobs") # HTML에서 class명이 jobs인 모든 sections 태그 가져오기