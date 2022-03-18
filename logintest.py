import signuptest

driver = signuptest.driver
driver.implicitly_wait(10)
driver.get('https://www.phptravels.net/login')
driver.find_element_by_xpath('//input[@name="email"]').send_keys(signuptest.my_email)
driver.find_element_by_xpath('//input[@name="password"]').send_keys(signuptest.my_password)

driver.find_element_by_xpath('//*[@id="fadein"]/div[1]/div/div[2]/div[2]/div/form/div[3]/button').click()

selenium_url = driver.current_url


