# CONSTANT
import inspect



URL = "http://www.theTestingWorld.com/testings"
USERNAME = "Admin"
PASSWORD = "admin123"
EMAIL = "123@hotmail.com"
# get testing name
def whoami():
    return inspect.stack()[1][3]