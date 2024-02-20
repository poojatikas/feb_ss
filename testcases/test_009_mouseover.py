import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class Test_009_mouse_over():

    def test_mouseover(self):

        driver = webdriver.Chrome()
        time.sleep(1)

        driver.maximize_window()
        time.sleep(1)

        driver.implicitly_wait(3)
        time.sleep(1)

        driver.get('https://www.google.com')
        time.sleep(1)

        driver.find_element(By.XPATH,'//textarea[@class="gLFyf"]').send_keys('Vtiger')
        time.sleep(1)

        driver.find_element(By.XPATH,'(//input[@class="gNO89b"])[1]').click()
        time.sleep(1)

        driver.find_element(By.XPATH,'(//h3[@class="LC20lb MBeuO DKV0Md"])[1]').click()
        time.sleep(1)

        action = ActionChains(driver)

        resource_tab = driver.find_element(By.XPATH,"//a[contains (text(),'Resources')]")
        action.move_to_element(resource_tab).perform()

        driver.save_screenshot("D:\\pythonProject1\\pythonProject1\\Final Revision\\screenshots\\test_009_mouseover.png")

        driver.find_element(By.XPATH,"//div[@class='col-4 p-lg-5']//a[@class='list-link'][normalize-space()='Contact Us']").click()
        time.sleep(1)

        contact = driver.find_element(By.XPATH,'(//div[@class="text-reset text-decoration-none"])[1]').text

        print('\n*********CONTACT INFORMATION**********')

        print('\n',contact)

        driver.close()


