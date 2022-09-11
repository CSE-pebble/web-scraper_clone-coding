from requests import get
from bs4 import BeautifulSoup

def extract_wwr_jobs(keyword): 
  base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="

  response = get(f"{base_url}{keyword}")
  if response.status_code != 200:
    print("Can't request website")
  else:
    results = []
    soup = BeautifulSoup(response.text, "html.parser") # HTML 다 가져옴
    jobs = soup.find_all("section", class_="jobs") # HTML에서 class명이 jobs인 모든 sections 태그 가져오기 -> 리스트에 들어감
    for job_section in jobs: 
      job_posts = job_section.find_all('li')
      job_posts.pop(-1)
      for post in job_posts:
        anchors = post.find_all('a')
        anchor = anchors[1] # 두번째 anchor에만 관심 있음
        link = anchor['href'] # beautifulsoup에서 dictionary 형태로 저장하기 때문에 href에 있는 값을 이와같이 가져올 수 있음
        company, kind, region = anchor.find_all('span', class_="company") # list로 반환되므로 각 요소 변수에 저장
        title = anchor.find('span', class_='title') #find_all이 아닌 find로 찾아오면 리스트로 반환X
        job_data = {
          'company': company.string,
          'region': region.string,
          'position': title.string
        }
        results.append(job_data)
    return results