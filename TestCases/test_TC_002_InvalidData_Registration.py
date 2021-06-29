from Base import InitiateDriver
from Library import ConfigReader
from utils import utils as ut

def test_registration_invalid_data():
    driver = InitiateDriver.start_browser()
    driver.find_element_by_name(ConfigReader.fetchElementLocator('Registration', 'username_name')).send_keys (ut.USERNAME)
    driver.find_element_by_name(ConfigReader.fetchElementLocator('Registration','password_name')).send_keys(ut.PASSWORD)
    driver.find_element_by_name(ConfigReader.fetchElementLocator('Registration', 'email_name')).send_keys(ut.EMAIL)
    driver.close()
    driver.quit()

