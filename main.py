from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import os
from dotenv import load_dotenv
import time 

load_dotenv()
LINKEDIN_USERNAME = os.environ.get('linkedin_username')
LINKEDIN_PASSWORD = os.environ.get('linkedin_password')
options = Options()
#options.add_argument("--headless=new")
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get('https://www.linkedin.com/jobs/search/?currentJobId=3601543818&f_AL=true&f_E=3&geoId=106057199&keywords=desenvolver%20python&location=Brazil&refresh=true&sortBy=R')

login_button = driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]')
login_button.click()

email_field = driver.find_element(By.ID, 'username')
email_field.send_keys(LINKEDIN_USERNAME)

password_field = driver.find_element(By.ID, 'password')
password_field.send_keys(LINKEDIN_PASSWORD)

password_field.send_keys(Keys.ENTER)

job_element_list = driver.find_elements(By.CSS_SELECTOR, '#main > div > div.scaffold-layout__list > div > ul > li')
for element in job_element_list:
    time.sleep(1)
    try:
        time.sleep(1)
        element.click()
        time.sleep(1)
        application_button = driver.find_element(By.CLASS_NAME, 'jobs-apply-button').click()
        apply_button = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div/form/footer/div[3]/button').click()
    except NoSuchElementException:
        try:
            close_button = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/button').click()
            time.sleep(1)
            discard_button = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[3]/button[1]/span').click()
        except NoSuchElementException:
            continue
