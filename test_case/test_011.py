import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture()
def setup():
    options = Options()
    options.binary_location = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
    driver = webdriver.Firefox(options=options)
    # driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://automation.credence.in")
    return driver


def pytest_metadata(metadata):
    # To Add
    metadata["Class"] = "Credence"
    metadata["Batch"] = "CT#15"
    metadata["URL"] = "https://automation.credence.in"
    # To Remove
    metadata.pop("Platform", None)

# How to edit Summary in html report this is your today's task

# use parameter when you have small data set
@pytest.fixture(params=[
    ("Credencetest@test.com","Credence@123"),
    ("Credencetest@test.com1","Credence@123"),
    ("Credencetest@test.com","Credence@1231"),
    ("Credencetest@test.com1","Credence@1231")
])
def getDataforLogin(request):
    return request.param