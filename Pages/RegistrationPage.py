from Library import ConfigReader

class RegistrationClass():

    def __init__(self, obj):
        global driver
        driver = obj
        # self.driver = driver

        self.username = ConfigReader.fetchElementLocator('Registration', 'username_name')
        self.password = ConfigReader.fetchElementLocator('Registration', 'password_name')
        self.email = ConfigReader.fetchElementLocator('Registration', 'email_name')

    def enter_username(self, username):
        driver.find_element_by_name(self.username).send_keys(username)

    def enter_password(self, password):
        driver.find_element_by_name(self.password).send_keys(password)

    def enter_email(self, email):
        driver.find_element_by_name(self.email).send_keys(email)