
class Test_Checkout:
    def test_Checkout(self):
        import time

        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.select import Select

        # Open Browser
        driver = webdriver.Chrome()

        # Go to Login page
        driver.get("https://automation.credence.in/login")
        driver.maximize_window()
        # time.sleep(1)

        # Enter Mail id With Xpath
        driver.find_element(By.XPATH, "//input[@type='email']").send_keys("CredenceJun_27@gmail.com")
        # time.sleep(1)

        # Enter Password With CSS Selector
        driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("CredenceJun_27")
        # time.sleep(1)

        # CLick on Login Button
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        # time.sleep(1)

        # Click on Apple Macbook Pro
        driver.find_element(By.XPATH, "/html/body/div/div[2]/div[3]/div/div/a[2]/h3").click()
        # Add to Cart Apple Macbook Pro
        driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
        # time.sleep(1)

        # Continue Shopping
        driver.find_element(By.XPATH, "//a[@class='btn btn-primary btn-lg']").click()
        # time.sleep(1)

        # Click on Headphones
        driver.find_element(By.XPATH, "//h3[normalize-space()='Headphones']").click()
        # Add to Cart Headphones
        driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
        # time.sleep(1)

        # Continue Shopping
        driver.find_element(By.XPATH, "//a[@class='btn btn-primary btn-lg']").click()

        # Click on Apple iPad Retina
        driver.find_element(By.XPATH, "//h3[normalize-space()='Apple iPad Retina']").click()
        # Add to Cart Apple iPad Retina
        driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
        # time.sleep(1)

        drp1 = Select(driver.find_element(By.XPATH, "//tbody/tr[1]/td[3]/select[1]"))
        # drp1.select_by_index(1)
        driver.implicitly_wait(10)

        drp2 = Select(driver.find_element(By.XPATH, "//tbody/tr[2]/td[3]/select[1]"))
        # drp2.select_by_index(1)
        driver.implicitly_wait(10)

        drp3 = Select(driver.find_element(By.XPATH, "//tbody/tr[3]/td[3]/select[1]"))
        # drp3.select_by_index(1)
        driver.implicitly_wait(10)

        driver.find_element(By.XPATH, "//a[normalize-space()='Proceed to Checkout']").click()
        driver.implicitly_wait(10)

        # Billing Details
        driver.find_element(By.NAME, "first_name").send_keys("Cre")
        driver.find_element(By.NAME, "last_name").send_keys("dence")
        driver.find_element(By.NAME, "phone").send_keys("1234567890")
        driver.find_element(By.NAME, "address").send_keys("Maharashtra Pune Kiwale 412102")
        driver.find_element(By.NAME, "zip").send_keys("412101")
        driver.implicitly_wait(10)
        state = Select(driver.find_element(By.NAME, "state"))
        state.select_by_visible_text("Pune")
        driver.implicitly_wait(10)

        # Payment Details
        driver.find_element(By.XPATH, "//input[@id='owner']").send_keys("Credence")
        driver.find_element(By.XPATH, "//input[@id='cvv']").send_keys("043")
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("5281")
        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("0370")
        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("4891")
        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("6168")

        time.sleep(2)
        # driver.implicitly_wait(10)

        Expiry_Year = Select(driver.find_element(By.ID, "exp_year"))
        Expiry_Year.select_by_index(3)
        time.sleep(2)
        # driver.implicitly_wait(10)

        Expiry_Month = Select(driver.find_element(By.ID, "exp_month"))
        Expiry_Month.select_by_index(1)
        time.sleep(2)
        # driver.implicitly_wait(10)

        # Continue Button
        driver.find_element(By.ID, "confirm-purchase").click()
        time.sleep(2)
        driver.close()
        # driver.implicitly_wait(10)
        # Alert = driver.switch_to.alert
        # Alert.accept()
        # time.sleep(2)