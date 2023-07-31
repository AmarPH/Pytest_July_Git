# 28-07-2023

# PYTEST FIRST TESTCASE

class Test_Credence:

    def test_fun_01(self):
        a = 3
        b = 3
        c = a * b
        print("Multiplication of A & B :", c)
        if c == 9:
            print("Right answer")
            assert True
        else:
            print("Wrong answer")
            assert False

    # def test_sel_02(self):
    #     from selenium import webdriver
    #     driver = webdriver.Chrome()
    #     driver.get("https://credence.in/")
    #     if driver.title == "Credence":
    #         print("Credence")
    #         assert True
    #     else:
    #         print("No Element Found")
    #         assert False

    # def test_sub_03(self):
    #     a = 5
    #     b = 4
    #     c = a - b
    #     print("Subtraction of A & B :", c)
    #     if c == 9:
    #         print("Right answer")
    #         assert True
    #     else:
    #         print("Wrong answer")
    #         assert False
#
# import time
# from selenium import webdriver
# from selenium.common import NoSuchElementException
# from selenium.webdriver.common.by import By
#
# # Open Browser
# driver = webdriver.Chrome()
#
# # Go to Login page
# driver.get("https://automation.credence.in/login")
# driver.maximize_window()
# time.sleep(2)
#
# # Enter Mail id With Xpath
# driver.find_element(By.XPATH, "//input[@type='email']").send_keys("CredenceJune_27@gmail.com")
# time.sleep(2)
#
# # Enter Password With CSS Selector
# driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("CredenceJun_27")
# time.sleep(2)
#
# # CLick on Login Button
# driver.find_element(By.XPATH, "//button[@type='submit']").click()
# time.sleep(1)
#
# try:
#     driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
#     print("Login Passed")
# except NoSuchElementException:
#     print("Login Failed")