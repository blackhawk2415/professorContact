from bs4 import BeautifulSoup
from selenium import webdriver
import re, time, random



with open('collegeList.txt', 'r') as file:
    searchTargets = file.read().splitlines()

linkTarget = ['//*[@id="rso"]/div[2]/li[2]/div/h3/a', '//*[@id="rso"]/div[2]/li[1]/div/h3/a']
emails = []
length, added, difference, counter = 0, 0, 0, 0

driverPath = '#'   # 'phantomjs  #change DIR to point to browser on local machine.
driver = webdriver.Chrome(executable_path=driverPath)
driver.set_page_load_timeout(12)

for searchTerm in searchTargets:
    error, loopVariant = 0, 0
    driver.get("https://www.google.com/#q="+searchTerm+"+international+relations+faculty")
    time.sleep(random.randrange(1, 2))
    print "Processing: " + searchTerm
    for target in linkTarget:
        time.sleep(1)
        try:
            driver.find_element_by_xpath(target).click()
            html = BeautifulSoup(driver.page_source)
            time.sleep(random.randrange(2, 3))
            emailList = html.findAll(text=re.compile(r'[A-Za-z0-9._]+@[A-Za-z._]+\.edu'))
            emails.append(emailList)
            driver.implicitly_wait(1)
        except:
            loopVariant += 1
            break
        loopVariant += 1
        if len(emailList) == 0:
            error += 1
        if loopVariant == 1:
            driver.back()
            time.sleep(random.randrange(2, 3))
    if error > 1:
        with open('failed.txt', 'a') as failedURLS:
            failedURLS.write(driver.current_url + '\n')

driver.quit()

print "Writing Emails to Doc."

output = open('emails.txt', 'a')
for emailArray in emails:
    for email in emailArray:
        if len(email) > 0:
            email = email.encode('ascii', 'ignore')
            output.write(email + '\n')

print "Saving results...Completed"
output.close()






































