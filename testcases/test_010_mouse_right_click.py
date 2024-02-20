import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert

class Test_010_mouse_rightclick():

    def test_010_right_click(self):

        driver = webdriver.Chrome()
        time.sleep(1)

        driver.maximize_window()
        time.sleep(1)

        driver.implicitly_wait(5)

        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        time.sleep(1)

        action = ActionChains(driver)

        right_click = driver.find_element(By.XPATH, '//span[text()="right click me"]')
        action.context_click(right_click).perform()

        time.sleep(3)

        driver.save_screenshot("D:\\pythonProject1\\pythonProject1\\Final Revision\\screenshots\\test_010_right_click.png")

        driver.find_element(By.XPATH,"//span[contains(text() ,'Edit')]").click()
        time.sleep(1)

        text1 = Alert(driver).text
        print('\n---------------TEXT AFTER RIGHT CLICK-----------')
        print('\n',text1)

        Alert(driver).accept()
        time.sleep(1)

        driver.close()


