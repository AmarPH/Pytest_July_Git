

class Test_Cred:
    def test_Registration(self):
        import time
        from selenium import webdriver
        from selenium.common import NoSuchElementException
        from selenium.webdriver.common.by import By

        # Open Browser
        driver = webdriver.Chrome()

        # Go To Register Link
        driver.get("https://automation.credence.in/register")
        driver.maximize_window()

        # Enter Name
        driver.find_element(By.NAME, "name").send_keys("CredenceJly_27")
        time.sleep(2)

        # Enter Email
        driver.find_element(By.NAME, "email").send_keys("CredenceJly_27@gmail.com")
        time.sleep(2)

        # Enter Password
        driver.find_element(By.ID, "password").send_keys("CredenceJly_27")
        time.sleep(2)

        # Enter Confirm Password
        driver.find_element(By.ID, "password-confirm").send_keys("CredenceJly_27")
        time.sleep(2)

        # Click On Register Button
        driver.find_element(By.CLASS_NAME, "btn").click()
        time.sleep(2)

        try:
            driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
            print("Registration Passed")
            assert True
        except NoSuchElementException:
            print("Registration Failed")
            driver.close()
            assert False


