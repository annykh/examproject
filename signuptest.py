from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome()
action = ActionChains(driver)
driver.maximize_window()
driver.implicitly_wait(10)

main_url = 'https://www.phptravels.net/'

driver.get(main_url)
my_email = 'anny.khyan@mail.ru'
my_fname = 'Anny'
my_lanme = 'Khachaturyan'
my_password = 'A123#456'
driver.find_element_by_xpath('//a[@href="https://www.phptravels.net/signup"]').click()
driver.find_element_by_xpath('//input[@name="first_name"]').send_keys(my_fname)
driver.find_element_by_xpath('//input[@name="last_name"]').send_keys(my_lanme)
driver.find_element_by_xpath('//input[@name="phone"]').send_keys('+37477110870')
driver.find_element_by_xpath('//input[@name="email"]').send_keys(my_email)
driver.find_element_by_xpath('//input[@name="password"]').send_keys(my_password)
sleep(5)
driver.execute_script("window.scrollTo(0, 600)")
sleep(5)
driver.find_element_by_xpath('//button[@type="submit"]').click()
sleep(5)
selenium_url = driver.current_url
