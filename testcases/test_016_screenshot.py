import time

from selenium import webdriver

class Test_016_screenshot():

    def test_016_ss(self):

        driver = webdriver.Chrome()
        time.sleep(1)

        driver.maximize_window()
        time.sleep(1)

        driver.implicitly_wait(5)
        time.sleep(1)

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(1)

        if(driver.title=='OrangeHRM'):
            driver.save_screenshot("D:\\pythonProject1\\pythonProject1\\Final Revision\\screenshots\\test_016_screenshot_pass.png")

            print('\n-----------YOU ARE AT HOME PAGE-----------')
            driver.close()
            assert True

        else:
            driver.save_screenshot("D:\\pythonProject1\\pythonProject1\\Final Revision\\screenshots\\test_016_screenshot_fail.png")
            print('\n-----------YOU ARE AT WRONG PAGE------------')
            driver.close()
            assert False



    def test_016_sum(self):

        a=20
        b=10
        sum = a+b
        if(sum==30):
            print('\n------------ADDITION IS SUCESSGFUL----------')
            print('\nRESULTS = ',sum)
            assert True
        else:
            print('\n------------ADDITION IS NOT POSSIBLE----------')

            assert False
#


#
# pytest -v -s -W ignore "testcases/test_016_screenshot.py" --html = "reports/Report.html" --alluredir = "D:\pythonProject1\pythonProject1\Final Revision\allure-results"