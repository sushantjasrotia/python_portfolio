from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://login.yahoo.com/?.intl=in&.lang=en-IN&src=ym&activity=mail-direct&pspid=159600001&done=https%3A%2F%2Fmail.yahoo.com%2Fd&add=1")

user_name = driver.find_element(By.NAME, value="username")
user_name.send_keys("sushantyes@yahoo.com", Keys.ENTER)

time.sleep(3)

password = driver.find_element(By.NAME, value="password")
password.send_keys("Nokia?tl3")

submit = driver.find_element(By.NAME, value="verifyPassword").click()

time.sleep(3)

#sending of mail
compose_mail = driver.find_element(By.XPATH, value='//*[@id="app"]/div[2]/div/div[1]/nav/div/div[1]/a').click()

time.sleep(1)

to_address = driver.find_element(By.XPATH, value='//*[@id="message-to-field"]')
to_address.send_keys("vikasrana2510@gmail.com")
time.sleep(2)
subject = driver.find_element(By.XPATH, value='//*[@id="compose-subject-input"]')
subject.send_keys("automated mail")
time.sleep(2)
body_of_mail = driver.find_element(By.XPATH, value='//*[@id="editor-container"]/div[1]')
body_of_mail.send_keys("hi vikas rana  \n\n"
                       "this is automated mail by pthon selinium please not reply to this \n\n"
                       "form Sushant Jasrotia")

#press send key manually



