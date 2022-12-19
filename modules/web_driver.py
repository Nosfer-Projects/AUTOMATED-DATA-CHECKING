from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class Search():
    @staticmethod
    def search(driver, path):
        return WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, path)))

