import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


class Test_002_demo_guru_details():

    def test_002_details(self):

        driver = webdriver.Chrome()
        time.sleep(1)

        driver.maximize_window()
        time.sleep(1)

        driver.implicitly_wait(5)

        driver.get("https://demo.guru99.com/V4/")
        time.sleep(1)

        driver.find_element(By.XPATH,"//input[@name='uid']").send_keys("mngr546290")
        time.sleep(1)

        driver.find_element(By.XPATH,'//input[@name="password"]').send_keys('vAhudYm')
        time.sleep(1)

        driver.find_element(By.XPATH,'//input[@name="btnLogin"]').click()
        time.sleep(1)

        if (driver.title== 'Guru99 Bank Manager HomePage'):
            driver.save_screenshot("D:\\pythonProject1\\pythonProject1\\Final Revision\\screenshots\\test_002_details_pass.png")
            time.sleep(1)

            print("************LOGIN SUCESSFULLY***********")
            time.sleep(1)

            print1 = driver.find_element(By.XPATH,'//td[@style="color: green"]').text
            print('\n******Details******')
            print('\n', print1)
            print('\n*************')

            driver.find_element(By.XPATH,"//a[contains(text(),'Log out')]").click()
            time.sleep(1)

            Alert(driver).accept()
            time.sleep(1)

            driver.close()
            assert True

        else:
            driver.save_screenshot("D:\\pythonProject1\\pythonProject1\\Final Revision\\screenshots\\test_002_details_fail.png")
            time.sleep(1)

            print('\n*******LOGIN UNCESSFULLY')

            driver.close()
            assert False














