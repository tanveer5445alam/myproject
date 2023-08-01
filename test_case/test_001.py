from selenium import webdriver


class Test_001:
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
