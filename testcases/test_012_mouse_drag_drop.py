import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class Test_012_mouse_Drag_Drop():

    def test_012_drag_drop(self):

        driver= webdriver.Chrome()
        time.sleep(1)

        driver.maximize_window()
        time.sleep(1)

        driver.implicitly_wait(5)

        driver.get("https://demo.automationtesting.in/Static.html")
        time.sleep(1)

        driver.save_screenshot("D:\\pythonProject1\\pythonProject1\\Final Revision\\screenshots\\test_012_drag_drop_before.png")

        driver.execute_script("window.scrollBy(0,300)")
        time.sleep(1)

        action= ActionChains(driver)

        src = driver.find_element(By.XPATH,'//img[@id="mongo"]')
        dest = driver.find_element(By.XPATH,'//div[@id="droparea"]')

        action.drag_and_drop(src , dest).perform()
        time.sleep(1)

        driver.save_screenshot("D:\\pythonProject1\\pythonProject1\\Final Revision\\screenshots\\test_012_mouse_drag_drop_after.png")

        driver.close()




