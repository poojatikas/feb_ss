import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_007_Explicit_wait():

    def test_007_exp_wait(self):

        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.get("https://www.google.com")

        driver.find_element(By.XPATH,'//textarea[@jsname="yZiJbe"]').send_keys("internet speed test")
        time.sleep(1)

        driver.find_element(By.XPATH,'(//input[@class="gNO89b"])[1]').click()
        time.sleep(1)

        driver.find_element(By.XPATH,"//div[contains(text(),'RUN SPEED TEST')]").click()

        try:
            wait = WebDriverWait(driver, 30, poll_frequency=0.5)
            wait.until(expected_conditions.visibility_of_element_located((By.XPATH,'(//div[@class="lv7K9c"])[3]')))

            print('\n-----------DOWNLOAD SPEED-----------')
            download = driver.find_element(By.XPATH,'//div[@class="oyUhj"]').text
            print(download)

            print('\n----------UPLOAD SPEED--------------')
            upload = driver.find_element(By.XPATH,'//div[@class="iD3Ij"]').text
            print(upload)

            driver.save_screenshot("D:\\pythonProject1\\pythonProject1\\Final Revision\\screenshots\\test_007_explicit_wait_pass.png")

            driver.close()
            assert True


        except:

            print('----------SORRY,SOMETHING WENT WRONG , PLEASE TRY LATER------------')
            driver.save_screenshot("D:\\pythonProject1\\pythonProject1\\Final Revision\\screenshots\\test_007_explicit_wait_fail.png")

            driver.close()
            assert False




