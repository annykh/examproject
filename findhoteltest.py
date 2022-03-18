import logintest
from time import sleep

driver = logintest.driver
driver.implicitly_wait(10)

driver.find_element_by_xpath('//*[text()="Hotels"]').click()
driver.find_element_by_xpath('//*[@id="select2-hotels_city-container"]').click()
driver.find_element_by_xpath('//*[@id="fadein"]/span/span/span[1]/input').send_keys("Yerevan")
driver.find_element_by_xpath('//*[text()="Yerevan,Armenia"]').click()
driver.find_element_by_xpath('//*[@id="hotels-search"]/div/div/div[3]/div/div/div/a').click()
driver.find_element_by_xpath('//div[@class="roomInc"]').click()
driver.find_element_by_xpath('//*[@id="nationality"]').click()
driver.find_element_by_xpath('//option[@value="AM"]').click()
driver.find_element_by_xpath('//*[@type="submit"]').click()
sleep(5)
driver.execute_script("window.scrollTo(0, 100)")
sleep(3)
driver.find_element_by_xpath('//label[@for="stars_4"]').click()
sleep(2)
get_url = driver.find_element_by_xpath('//*[@id="opera suite hotel"]/div/div[2]/div/div[2]/div/a').get_attribute("href")
sleep(5)
driver.get(get_url)

driver.execute_script("window.scrollTo(0, 100)")
get_url = driver.find_element_by_xpath('//*[@id="contentContainer"]/div[3]/ol/li[1]/div[2]/a').get_attribute("href")
driver.get(get_url)

driver.find_element_by_xpath('//button[text()="Book now"]').click()
sleep(5)
selenium_url = driver.current_url
