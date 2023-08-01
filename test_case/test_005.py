from selenium import webdriver


class Test_002:
    def test_Credence_001(self):
        driver = webdriver.Chrome()
        driver.get("https://credence.in/")
        if driver.title == "Credence":
            driver.save_screenshot("D:\\Credence Class Notes\\CredenceBatches\\CredenceBatch#14 & 15\\Pytest_Demo\\Screenshots\\Credence.PNG")
            driver.close()
            assert True
        else:
            print("You are at wrong place")
            driver.close()
            assert False


    def test_sum_0012(self):
        a = 2
        b = 5
        sum = a+b
        print("This is sum of a&b: " + str(sum))
        if sum == 7:
            assert True
        else:
            assert False
    def test_div_0022(self):
        a = 20
        b = 5
        div = a/b
        print("This is sum of a&b: " + str(div))
        if div == 4:
            assert True
        else:
            assert False
