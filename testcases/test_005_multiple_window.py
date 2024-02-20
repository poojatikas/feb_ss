import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_005_multiple_window_handle():

    def test_005_handle_multiple_window(self):

        driver = webdriver.Chrome()
        time.sleep(1)

        driver.maximize_window()
        time.sleep(1)

        driver.implicitly_wait(5)
        time.sleep(1)

        driver.get("https://the-internet.herokuapp.com/windows")
        time.sleep(1)

        driver.find_element(By.XPATH,"//a[text()='Click Here']").click()
        time.sleep(1)

        multiple_window = driver.window_handles
        time.sleep(1)

        driver.switch_to.window(multiple_window[1])
        print('\n------TEXT IN CHILD WINDOW------')
        text1 = driver.find_element(By.XPATH,"//h3[text() = 'New Window']").text
        print('\n', text1)
        driver.save_screenshot("D:\\pythonProject1\\pythonProject1\\Final Revision\\screenshots\\test_005_child_window.png")
        time.sleep(1)

        driver.switch_to.window(multiple_window[0])
        print('\n--------TEXT IN PARENT WINDOW--------')
        text2 = driver.find_element(By.XPATH,"//h3[text()='Opening a new window']").text
        print('\n',text2)
        driver.save_screenshot("D:\\pythonProject1\\pythonProject1\\Final Revision\\screenshots\\test_005_parent_winow.png")
        time.sleep(1)

        driver.close()


