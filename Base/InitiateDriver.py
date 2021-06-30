from selenium.webdriver import Chrome, Firefox
from Library import ConfigReader

def start_browser():
    global driver
    if (ConfigReader.readConfigData('Details', 'Browser')) == "chrome":
        path = "C:\\Selenium\\EndToEndAutomation\\drivers\\chromedriver.exe"
        driver = Chrome(executable_path=path)
    elif ConfigReader.readConfigData('Details', 'Browser') == "firefox":
        path = "C:\\Selenium\\EndToEndAutomation\\drivers\\geckodriver.exe"
        driver = Firefox(executable_path=path)
    else:
        path = "C:/Selenium/EndToEndAutomation/drivers/chromedriver.exe"
        driver = Chrome(executable_path=path)

    driver.get(ConfigReader.readConfigData('Details','URL'))
    driver.implicitly_wait(30)
    driver.maximize_window()
    return driver

def close_browser():
    driver.close()
    driver.quit()