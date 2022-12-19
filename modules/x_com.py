from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import sys

from modules.web_driver import Search



list_of_pcs = []

class Xkom:
    def __init__(self, path, price):

        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=path, chrome_options=options)
        self.price = price

    def find_pc(self):
        self.driver.get("https://www.x-kom.pl/")
        cookie = Search.search(self.driver, '//*[@id="react-portals"]/div[11]/div/div/div/div[3]/button[2]')
        cookie.click()
        pc_option =Search.search(self.driver, '//*[@id="app"]/div[1]/header/div[2]/div/div/div/nav/ul/li[1]')
        pc_option.click()
        gamer_pc = Search.search(self.driver, '//*[@id="app"]/div[1]/header/div[2]/div/div/div/nav/ul/li[1]/section/div/div[1]/div[2]/ul/li[6]/a')
        gamer_pc.click()
        cost =Search.search(self.driver, '//*[@id="listing-filters"]/div[2]/div/section[2]/div/div/div/div[2]/div/input')
        cost.send_keys(self.price)


    def web_data(self):
        time.sleep(3)
        try:
            items = self.driver.find_element(By.XPATH, '//*[@id="listing-container-wrapper"]/div[4]/div[1]/div/div[2]').text
            number_of_items = int(items.split(" ")[2])
            for n in range(number_of_items):
                try:
                    price = self.driver.find_element(By.XPATH, f'//*[@id="listing-container"]/div[{n + 1}]/div/div[2]/div[3]/div/div[2]/div/div/span[2]').text

                except:
                    price = self.driver.find_element(By.XPATH, f'//*[@id="listing-container"]/div[{n + 1}]/div/div[2]/div[3]/div/div[2]/div/div/span').text


                specification = self.driver.find_element(By.XPATH, f'//*[@id="listing-container"]/div[{n + 1}]/div/div[2]/div[2]/ul').text


                link = self.driver.find_element(By.XPATH, f'//*[@id="listing-container"]/div[{n + 1}]/div/div[2]/div[2]/div[1]/a').get_attribute("href")
                pc = {}
                pc["Price"] = price
                pc["Specification"] = specification
                pc["Link"] = link
                list_of_pcs.append(pc)
            print("\n\nPrepares data in excel format. Please wait...")    
            self.driver.close()
            return list_of_pcs
        except:
            check_amount = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div[2]/div/div/div[2]/div[1]').text
            if check_amount == "Przepraszamy, nie znaleźliśmy tego, czego szukasz":
                print("Sorry, we couldn't find what you're looking for.")
            self.driver.close()
            sys.exit()
