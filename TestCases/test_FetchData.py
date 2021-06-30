from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as ec
import time
import pytest

@pytest.fixture()
def environment_setup():
    global driver
    path = "C:\\Selenium\\EndToEndAutomation\\drivers\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("http://www.theTestingWorld.com/testings")
    driver.refresh()
    # run java script
    driver.execute_script("window.scrollTo(0,380);")
    # Maximize browser
    # driver.implicitly_wait(20)
    driver.maximize_window()
    yield
    driver.close()

def test_verify_registration(environment_setup):
    #  Work on Dropdown
    wait  = WebDriverWait(driver,100)
    wait.until(ec.text_to_be_present_in_element((By.ID,'countryId'),"India"))
    obj = Select(driver.find_element_by_id("countryId"))

    obj.select_by_visible_text("India")

    wait.until(ec.text_to_be_present_in_element((By.ID, 'stateId'), "Delhi"))
    obj = Select(driver.find_element_by_id("stateId"))
    obj.select_by_visible_text("Delhi")

@pytest.mark.skip("Skip test case")
# pytest -k name test case (execute specification test case)
# pytest -m "not name test case (except execute test case)
def test_verify(environment_setup):
    #  Work on Dropdown
    wait  = WebDriverWait(driver,100)
    wait.until(ec.text_to_be_present_in_element((By.ID,'countryId'),"India"))
    obj = Select(driver.find_element_by_id("countryId"))

    obj.select_by_visible_text("India")

    wait.until(ec.text_to_be_present_in_element((By.ID, 'stateId'), "Delhi"))
    obj = Select(driver.find_element_by_id("stateId"))
    obj.select_by_visible_text("Delhi")