# 28-07-2023

# PYTEST FIRST TESTCASE

class Test_Credence:

    def test_Login(self):
        import time
        from selenium import webdriver
        from selenium.common import NoSuchElementException
        from selenium.webdriver.common.by import By

        # Open Browser
        driver = webdriver.Chrome()

        # Go to Login page
        driver.get("https://automation.credence.in/login")
        driver.maximize_window()
        time.sleep(2)

        # Enter Mail id With Xpath
        driver.find_element(By.XPATH, "//input[@type='email']").send_keys("CredenceJun_27@gmail.com")
        time.sleep(2)

        # Enter Password With CSS Selectorp
        driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("CredenceJun_27")
        time.sleep(2)

        # CLick on Login Button
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(1)

        try:
            driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
            print("Login Passed")
            assert True
        except NoSuchElementException:
            print("Login Failed")
            driver.close()
            assert False

