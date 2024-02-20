import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

class Test_001_Demo_login():

    def test_001_demp_login_guru99(self):
        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(5)

        driver.get("https://demo.guru99.com/V4/")
        time.sleep(2)

        driver.find_element(By.XPATH,'//input[@name="uid"]').send_keys('mngr546290')
        time.sleep(1)

        driver.find_element(By.XPATH,'//input[@name="password"]').send_keys('vAhudYm')
        time.sleep(1)

        driver.find_element(By.XPATH,'//input[@name="btnLogin"]').click()
        time.sleep(1)

        if (driver.title=='Guru99 Bank Manager HomePage') :
            time.sleep(1)
            driver.save_screenshot("D:\\pythonProject1\\pythonProject1\\Final Revision\\screenshots\\test_001_demo_login_pass.png")

            print('login Sucessfully')

            driver.find_element(By.XPATH,'//a[text()="Log out"]').click()
            time.sleep(1)

            Alert(driver).accept()
            time.sleep(1)

            driver.close()
            assert True

        else:
            driver.save_screenshot("D:\\pythonProject1\\pythonProject1\\Final Revision\\screenshots\\test_001_demo_login_fail.png")

            print('login Unsucessfully')

            driver.close()

            assert False



