import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert

class Test_011_doubleclick():

    def test_011_doubleclick(self):

        driver = webdriver.Chrome()
        time.sleep(1)

        driver.maximize_window()
        time.sleep(1)

        driver.implicitly_wait(5)

        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        time.sleep(1)

        action = ActionChains(driver)

        double_click = driver.find_element(By.XPATH,'//button[text() = "Double-Click Me To See Alert"]')
        action.double_click(double_click).perform()
        time.sleep(1)

        print('\n********TEXT AFTER DOUBLE CLICK********')
        text1 = Alert(driver).text
        print('\n',text1)

        Alert(driver).accept()
        time.sleep(1)

        driver.close()


