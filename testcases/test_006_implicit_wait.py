import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_006_Implicitwait():

    def test_006_impli_wait(self):

        driver = webdriver.Chrome()
        time.sleep(1)

        driver.maximize_window()
        time.sleep(1)

        driver.implicitly_wait(20)
        time.sleep(1)

        driver.get("https://www.google.com")
        time.sleep(1)

        driver.find_element(By.XPATH,'// textarea[ @ jsname = "yZiJbe"]').send_keys("Internet speed")
        time.sleep(1)

        driver.find_element(By.XPATH,'(//input[@class="gNO89b"])[1]').click()
        time.sleep(1)

        driver.find_element(By.XPATH,'(//div[contains(text(),"RUN SPEED TEST")]').click()
        time.sleep(25)

        print('\n ------Download Speed-------')
        Download = driver.find_element(By.XPATH,'//div[@class="oyUhj"]').text
        print(Download)

        print('\n-------Upload Speed-----------')
        Upload = driver.find_element(By.XPATH,'//div[@class="iD3Ij"]').text
        print(Upload)

        driver.save_screenshot("D:\\pythonProject1\\pythonProject1\\Final Revision\\screenshots\\test_006_implicit_wait_pass.png")


        driver.close()
