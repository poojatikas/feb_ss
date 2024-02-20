import time

from selenium import webdriver
from  selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Test_008_facebook_dd():

    def test_008_fb(self):

        driver = webdriver.Chrome()
        time.sleep(1)

        driver.maximize_window()
        time.sleep(2)

        driver.implicitly_wait(5)

        driver.get("https://www.facebook.com")
        time.sleep(2)

        driver.find_element(By.XPATH,'//a[@class="_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy"]').click()

        driver.find_element(By.XPATH,'//input[@placeholder="First name"]').send_keys('Priya')
        time.sleep(1)

        driver.find_element(By.XPATH,'//input[@name="lastname"]').send_keys('nandankar')
        time.sleep(1)

        driver.find_element(By.XPATH,'//input[@name="reg_email__"]').send_keys('priyanandankar@gmail.com')
        time.sleep(1)

        driver.find_element(By.XPATH,'//input[@aria-label="New password"]').send_keys('priya@123456')
        time.sleep(1)

        day = Select(driver.find_element(By.XPATH,'//select[@name="birthday_day"]'))
        day.select_by_index(10)
        time.sleep(2)

        month = Select(driver.find_element(By.XPATH,'//select[@name="birthday_month"]'))
        month.select_by_visible_text('Aug')
        time.sleep(2)

        year = Select(driver.find_element(By.XPATH,'//select[@name="birthday_year"]'))
        year.select_by_value('2000')

        time.sleep(2)

        driver.find_element(By.XPATH,'(//input[@type="radio"])[1]').click()

        driver.save_screenshot('D:\\pythonProject1\\pythonProject1\\Final Revision\\screenshots\\test_008_facebook_dd.png')

        driver.close()














