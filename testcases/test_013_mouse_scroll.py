import time

from selenium import webdriver

class Test_013_mousescroll():

    def test_013_scroll(self):

        driver = webdriver.Chrome()
        time.sleep(1)

        driver.maximize_window()
        time.sleep(1)

        driver.implicitly_wait(5)

        driver.get("https://www.bbc.com/")
        time.sleep(1)

        driver.save_screenshot("D:\\pythonProject1\\pythonProject1\\Final Revision\\screenshots\\test_013_mouse_scroll_before.png")
        time.sleep(1)

        driver.execute_script("window.scrollBy(0,1000)")

        driver.save_screenshot("D:\\pythonProject1\\pythonProject1\\Final Revision\\screenshots\\test_013_mouse_scroll_after.png")

        time.sleep(1)

        driver.close()



