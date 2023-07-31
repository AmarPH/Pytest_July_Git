# 28-07-2023


# PYTEST FIRST TESTCASE


import pytest
class Test_Credence:

    def test_add_01(self):
        a = 5
        b = 4
        c = a + b
        print("-------------------->Addition of A & B :", c)
        if c == 9:
            print("Right answer")
            assert True
        else:
            print("Wrong answer")
            assert False

    @pytest.mark.skip
    def test_cred_02(self):
        from selenium import webdriver
        driver = webdriver.Chrome()
        driver.get("https://credence.in/")
        if driver.title == "Credence":
            print("Credence")
            assert True
        else:
            print("No Element Found")
            assert False

    # @pytest.mark.Credence
    def test_sub_03(self):
        a = 5
        b = 4
        c = a - b
        print("-------------------->Subtraction of A & B :", c)
        if c == 1:
            print("Right answer")
            assert True
        else:

            print("Wrong answer")
            assert False

    @pytest.mark.skipif
    def test_mul_04(self):
        a = 3
        b = 3
        c = a * b
        print("-------------------->Multiplication of A & B :", c)
        if c == 9:
            assert True
            print("Correct Answer")
        else:
            print("Wrong Answer")
            assert False
