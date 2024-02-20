from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Test_008_drop_down():

    def test_008_drop_dowmn_insurance(self):

        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(10)

        driver.get("https://www.careinsurance.com/rhicl/proposalcp/renew/index-care")

        driver.find_element(By.XPATH,'//input[@name="policynumber"]').send_keys('123456789')

        driver.find_element(By.XPATH,'//input[@placeholder="DOB"]').click()

        month = Select(driver.find_element(By.XPATH,'//select[@aria-label="Select month"]'))
        month.select_by_index(6)

        year = Select(driver.find_element(By.XPATH,'//select[@aria-label="Select year"]'))
        year.select_by_value('2000')

        driver.find_element(By.XPATH,'//a[@data-date="16"]').click()

        driver.find_element(By.XPATH,'//input[@placeholder="Contact Number"]').send_keys('9878456321')

        driver.save_screenshot('D:\\pythonProject1\\pythonProject1\\Final Revision\\screenshots\\test_008_dropdown.png')

        driver.close()

