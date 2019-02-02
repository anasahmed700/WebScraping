from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome("./chromedriver", chrome_options=chrome_options)
driver.get('http://www.glassdoor.com/index.html')

driver.find_element_by_xpath("//*[@id='KeywordSearch']").send_keys("python")
driver.find_element_by_xpath('//*[@id="HeroSearchButton"]').click()
job_list = driver.find_elements_by_xpath("//ul[@class='jlGrid hover']/li")

# for job in job_list:
#     print(job.text)
keywords = ['python', 'data analyst']
jobs_outfile = open('./jobs.txt', 'w', encoding="utf-8")

for job in job_list:
    if 'Senior' in job.text:
        jobs_outfile.write(job.text)

jobs_outfile.close()
