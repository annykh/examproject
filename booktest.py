import findhoteltest
import unittest
from time import sleep

import signuptest

driver = findhoteltest.driver

driver.find_element_by_xpath('//*[@id="firstName_lastName"]').send_keys(signuptest.my_fname + " " + signuptest.my_lanme)
driver.find_element_by_xpath('//input[@name="email"]').send_keys(signuptest.my_email)
driver.find_element_by_xpath('//input[@name="retypeEmail"]').send_keys(signuptest.my_email)
driver.execute_script("window.scrollTo(0, 250)")
sleep(4)
driver.find_element_by_xpath('//*[@id="SiteContent"]/div/div[1]/div[3]/div/div[3]/div[1]/div[2]/label[4]').click()
driver.find_element_by_xpath('//button[@type="submit"]').click()
sleep(5)
selenium_url = driver.current_url
sleep(20)

driver.close()