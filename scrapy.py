# This is a simple python web scraper to grab LinkedIn profile data.
# Aim is to perform keyword analytics on the jobs I'm interested in.
# Reference: https://www.linkedin.com/pulse/how-easy-scraping-data-from-linkedin-profiles-david-craven/

# import web driver
from selenium import webdriver
import parameters
from time import sleep
from selenium.webdriver.common.keys import Keys
from parsel import Selector 
# Also requries: ipython, selenium, time, parsel, csv

# function to ensure all key data fields have a value
def validate_field(field):# if field is present pass if field:
       pass
# if field is not present print text else:
       field = 'No results'return field

# defining new variable passing two paramaters
writer = csv.writer(open(parameters.file_name, 'wb'))

# writerow() method to the write to the file object
writer.writerow(['Name', 'Job Title', 'Company', 'College', 'Location', 'URL'])

### Logging into LinkedIn
# specifies the path to the chromedriver.exe
driver = webdriver.Chrome('/Users/username/bin/chromedriver')

# driver.get method() will navigate to a page given by the URL address
driver.get(parameters.search_query)

# locate email form by_class_name
username = driver.find_element_by_class_name('login-email')

# send_keys() to simulate key strokes
username.send_keys(parameters.linkedin_username)

# sleep for 0.5 seconds
sleep(0.5)

# locate password form by_class_name
password = driver.find_element_by_class_name('login-password')

# send_keys() to simulate key strokes
password.send_keys(parameters.linkedin_password)
sleep(0.5)

# locate submit button by_xpath
sign_in_button = driver.find_element_by_xpath('//*[@type="submit"]')

# .click() to mimic button click
sign_in_button.click()

### Searching Google
driver.get('https://www.google.com')
sleep(3)
# locate search form by_name
search_query = driver.find_element_by_name('q')

# send_keys() to simulate the search text key strokes
search_query.send_keys('site:linkedin.com/in/ AND '+param_1+' AND '+param2)
sleep(0.5)

# .send_keys() to simulate the return key 
search_query.send_keys(Keys.RETURN)
sleep(3)

#  locate URL by_class_name
linkedin_urls = driver.find_elements_by_class_name('iUh30')

# variable linkedin_url is equal to the list comprehension 
linkedin_urls = [url.text for url in linkedin_urls]
sleep(0.5)

### Data extraction
# For loop to iterate over each URL in the list
for linkedin_url in linkedin_urls:

   # get the profile URL 
   driver.get(linkedin_url)

   # add a 5 second pause loading each URL
   sleep(5)

   # assigning the source code for the webpage to variable sel
   sel = Selector(text=driver.page_source) 

# terminates the application
driver.quit()

#xpath to extract the first h1 text 
name = sel.xpath('//h1/text()').extract_first()

# xpath to extract the exact class containing the text
name = sel.xpath('//*[starts-with(@class, "pv-top-card-section__name")]/text()').extract_first()

if job_title:
    # .strip() will remove the new line /n and white spaces
    job_title = job_title.strip()
    
# validating if the fields exist on the profile
name = validate_field(name)
job_title = validate_field(job_title)
company = validate_field(company)
college = validate_field(college)
location = validate_field(location)
linkedin_url = validate_field(linkedin_url)

# printing the output to the terminal
print('\n')
print('Name: ' + name)
print('Job Title: ' + job_title)
print('Company: ' + company)
print('College: ' + college)
print('Location: ' + location)
print('URL: ' + linkedin_url)
print('\n')

# writing the corresponding values to the header
writer.writerow([name.encode('utf-8'),
                 job_title.encode('utf-8'),
                 company.encode('utf-8'),
                 college.encode('utf-8'),
                 location.encode('utf-8'),
                 linkedin_url.encode('utf-8')])
