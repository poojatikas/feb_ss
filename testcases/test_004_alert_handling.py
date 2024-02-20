import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

class Test_004_handling_alert():

    # def test_004_alert(self):
    #
    #     driver = webdriver.Chrome()
    #     time.sleep(1)
    #
    #     driver.maximize_window()
    #     time.sleep(1)
    #
    #     driver.implicitly_wait(5)
    #     time.sleep(1)
    #
    #     print("\n*********FOR SIMPLE ALERT********")
    #
    #     driver.get("https://demoqa.com/alerts")
    #     time.sleep(1)
    #
    #     driver.find_element(By.XPATH,'//button[@id="alertButton"]').click()
    #     time.sleep(1)
    #
    #     alert1 = Alert(driver).text
    #     print("\n************Alert text******** ")
    #     print("\n",alert1)
    #     print('\n******************')
    #
    #     Alert(driver).accept()
    #     time.sleep(1)
    #
    #     print("\n **********ALERT ACCEPTED*******")
    #     driver.close()
    #
    # def test_004_confirmation_alert(self):
    #
    #     driver = webdriver.Chrome()
    #     time.sleep(1)
    #
    #     driver.maximize_window()
    #     time.sleep(1)
    #
    #     driver.implicitly_wait(5)
    #     time.sleep(1)
    #
    #     driver.get("https://demoqa.com/alerts")
    #     time.sleep(1)
    #
    #     print("\n*******CONFIRMATION ALERT*******")
    #
    #     driver.find_element(By.XPATH,"//button[@id='confirmButton']").click()
    #     time.sleep(1)
    #
    #     alert2 = Alert(driver).text
    #     print('\n*******ALERT TEXT******')
    #     print('\n',alert2)
    #
    #     Alert(driver).accept()
    #     print('\n*******ALERT ACCEPTED******')
    #
    #     print('\n*********TEXT ALERT AFTER ACCEPTANCE******')
    #     alert_result=driver.find_element(By.XPATH,'//span[@id="confirmResult"]').text
    #     print('\n******alert_result*******')
    #     print('\n***************')
    #
    #     driver.find_element(By.XPATH,'//button[@id="confirmButton"]').click()
    #     time.sleep(1)
    #
    #     alert3 = Alert(driver).text
    #     print('\n***********ALERT TEXT********')
    #     print('\n',alert3)
    #
    #     Alert(driver).dismiss()
    #
    #     print('\n*********ALERT DISMISSD*********')
    #
    #     print('\n*******TEXT AFTER ALERT DISSMISSAL*******')
    #     alert_result2= driver.find_element(By.XPATH,'//span[@id="confirmResult"]').text
    #     print('\n',alert_result2)
    #     print('\n************')
    #
    #     driver.close()

    def test_004_prompt_alert(self):

        driver = webdriver.Chrome()
        time.sleep(1)

        driver.maximize_window()
        time.sleep(1)

        driver.implicitly_wait(10)
        time.sleep(1)

        print('\n********PROMPT ALERT*********')

        driver.get("https://demoqa.com/alerts")
        time.sleep(1)

        driver.find_element(By.XPATH, '(//button[@id="promtButton"])').click()
        time.sleep(1)

        Alert(driver).send_keys('om sai ram')
        time.sleep(1)

        Alert(driver).accept()
        time.sleep(1)

        print('\n*************TEXT INSERTED**********')

        prompt_alert=driver.find_element(By.XPATH,"//span[@id='promptResult']").text
        print('\n',prompt_alert)
        print('*******************')

        driver.close()








