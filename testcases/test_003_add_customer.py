import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

class Test_003_add_cust_guru():

    def test_003_new_cust(self):

        driver = webdriver.Chrome()
        time.sleep(1)

        driver.maximize_window()
        time.sleep(1)

        driver.implicitly_wait(5)
        time.sleep(1)

        driver.get("https://demo.guru99.com/V4/index.php")
        time.sleep(1)

        driver.find_element(By.NAME, "uid").send_keys("mngr546290")
        time.sleep(1)

        driver.find_element(By.XPATH,"//input[@name='password']").send_keys("vAhudYm")
        time.sleep(1)

        driver.find_element(By.XPATH,"//input[@name='btnLogin']").click()
        time.sleep(1)

        if(driver.title=='Guru99 Bank Manager HomePage'):
            driver.save_screenshot("D:\\pythonProject1\\pythonProject1\\Final Revision\\screenshots\\test_003_add_customer_pass.png")

            print('************LOGIN SUCESSFULLY***********')

            driver.find_element(By.XPATH,"//a[text()='New Customer']").click()
            time.sleep(1)

            driver.find_element(By.XPATH,'//input[@name="name"]').send_keys('ADVIKA PATHAK')
            time.sleep(1)

            driver.find_element(By.XPATH,"//input[@value='f']").click()
            time.sleep(1)

            driver.find_element(By.ID,"dob").send_keys('22122000')
            time.sleep(1)

            driver.find_element(By.NAME,"addr").send_keys('plot no=5200, Line No-22,mahatma fule marg ,pune')
            time.sleep(1)

            driver.find_element(By.NAME,'city').send_keys("Pune")
            time.sleep(1)

            driver.find_element(By.NAME,'state').send_keys('Maharashtra')
            time.sleep(1)

            driver.find_element(By.NAME,'pinno').send_keys('561203')
            time.sleep(1)

            driver.find_element(By.NAME,"telephoneno").send_keys('9856214023123')
            time.sleep(1)

            driver.find_element(By.XPATH,'//input[@'
                                         'name="emailid"]').send_keys('abs@mngr546290')
            time.sleep(1)

            driver.find_element(By.XPATH,'//input[@name="password"]').send_keys('xyzvAhudYm')
            time.sleep(1)

            driver.find_element(By.XPATH,'//input[@type="submit"]').click()
            time.sleep(1)

            Alert(driver).accept()
            time.sleep(1)


            print('\n*****customer added sucessfully******')
            time.sleep(5)

            driver.save_screenshot(
                "D:\\pythonProject1\\pythonProject1\\Final Revision\\screenshots\\test_0003_added_customer_pass.png")
            time.sleep(1)

            driver.find_element(By.XPATH,"//a[normalize-space()='Log out']").click()
            time.sleep(1)

            Alert(driver).accept()
            time.sleep(1)

            driver.close()
            assert True

        else:
            driver.save_screenshot(
                "D:\\pythonProject1\\pythonProject1\\Final Revision\\screenshots\\test_0003_added_customer_fail.png")
            time.sleep(1)

            print('*******LOGINUNSUESSFUL*******')

            driver.close()
            assert False










