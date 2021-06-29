import pytest
from utils import utils as ut
from Base import InitiateDriver
from Pages.RegistrationPage import RegistrationClass
from Library import ConfigReader
import openpyxl
from DataGenerate import DataExcel


@pytest.mark.parametrize ('data', DataExcel.data_generate())
def test_validate_registration(data) :
    driver = InitiateDriver.start_browser ()
    register = RegistrationClass (driver)
    register.enter_username (data[0])
    register.enter_password (data[1])
    register.enter_email (ut.EMAIL)
    InitiateDriver.close_browser ()
