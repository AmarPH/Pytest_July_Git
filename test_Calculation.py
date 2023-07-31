
class Test_Calculation:
    def test_Cal(self):
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
        drp1.select_by_index(2)
        time.sleep(1)

        drp2 = Select(driver.find_element(By.XPATH, "//tbody/tr[2]/td[3]/select[1]"))
        drp2.select_by_index(3)
        time.sleep(1)

        drp3 = Select(driver.find_element(By.XPATH, "//tbody/tr[3]/td[3]/select[1]"))
        drp3.select_by_index(3)
        time.sleep(2)

        # l = len(driver.find_elements(By.XPATH, "//tbody/tr/td[4]")) # l = 6
        #
        # Product_Price_List =[]
        # for i in range(1, l-2):
        #     var1 = driver.find_element(By.XPATH, "//tbody/tr["+str(i)+"]/td[4]").text
        #     product_price = (var1[1:])
        #     Product_Price_List.append(float(product_price))
        # # print(Product_Price_List)
        #
        # Exp_Subtotal = round((sum(Product_Price_List)), 2)
        # # Exp_Subtotal-->11999.889999999998
        # # Exp_Subtotal-->11999.89
        # print("Exp_Subtotal-->" + str(Exp_Subtotal))
        # GrandTotal = round((Exp_Subtotal * 1.13),2)
        # print("Grand Total : ",GrandTotal)
        #
        #
        # System_Price = []
        # for i in range(l-2, l+1):
        #     var2 = driver.find_element(By.XPATH, "//tbody/tr["+str(i)+"]/td[4]").text
        #     var3 = var2.replace(',', '')
        #     # print(var3)
        #     system_price = (var2[1:])
        #     System_Price.append(system_price)
        #
        # print("System_Price : ",System_Price)
        # print("Tax : ", System_Price[1])
        # System_Total = System_Price[2].replace(",", "")
        # print("System Total : ",System_Total).
        # # time.sleep(2)
        #
        # if GrandTotal == System_Total[0]:
        #     print("SubTotal Matched")
        # else:
        #     print("Subtotal Not Matched")

        l = len(driver.find_elements(By.XPATH, "//tbody/tr/td[4]"))
        # l=6
        time.sleep(2)
        Product_Price_List = []
        for r in range(1, l - 2):
            var1 = driver.find_element(By.XPATH, "//tbody/tr[" + str(r) + "]/td[4]").text
            # print(var1)
            product_price = (var1[1:])
            # print(product_price)
            Product_Price_List.append(float(product_price))

        print("Product_Price_List :", Product_Price_List)
        Exp_Subtotal = round((sum(Product_Price_List)), 2)
        # Product_Price_List-->11999.889999999998 ----> After Round Of
        # Exp_Subtotal-->11999.89
        print("Exp_Subtotal-->", str(Exp_Subtotal))
        # print(Product_Price_List)

        System_Value = []
        for r in range(l - 2, l + 1):
            var2 = driver.find_element(By.XPATH, "//tbody/tr[" + str(r) + "]/td[4]").text
            # print("Var2 :", var2)
            var3 = var2.replace(',', '')
            # print("Var3 :", var3)
            system_price = (var3[1:])
            print("system_price :", system_price)
            System_Value.append(float(system_price))

        print("System_Value :", System_Value)

        GrandTotal = round((Exp_Subtotal * 1.13), 2)
        print("Grand Total :", GrandTotal)

        if GrandTotal == System_Value[2]:
            print("SubTotal is matched")
            assert True
        else:
            print("Subtotal is not matched")
            driver.close()
            assert False
