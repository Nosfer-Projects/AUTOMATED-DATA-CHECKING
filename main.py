from lib2to3.pgen2 import driver
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

chrome_driver_path = Service("[Path to your driver]")

price_pc = int(input("How much can you spend on buying a new gaming computer? Please enter the amount in the currency PLN : "))

list_of_pcs = []
class Xkom:
    def __init__(self, path):

        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=path, chrome_options=options)

    def find_pc(self):
        self.driver.get("https://www.x-kom.pl/")
        time.sleep(2)
        cookie = self.driver.find_element(By.XPATH, '//*[@id="react-portals"]/div[11]/div/div/div/div[3]/button[2]')
        cookie.click()
        pc_option = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/header/div[2]/div/div/div/nav/ul/li[1]')
        pc_option.click()
        gamer_pc = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/header/div[2]/div/div/div/nav/ul/li[1]/section/div/div[1]/div[2]/ul/li[6]/a')
        time.sleep(2)
        gamer_pc.click()
        time.sleep(2)
        cost = self.driver.find_element(By.XPATH, '//*[@id="listing-filters"]/div[2]/div/section[2]/div/div/div/div[2]/div/input')
        cost.send_keys(price_pc)
        time.sleep(3)


    def web_data(self):
        
        time.sleep(3)
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
            
        self.driver.close()

            
        
new_pc = Xkom(chrome_driver_path)
new_pc.find_pc()
new_pc.web_data()

df = pd.DataFrame(list_of_pcs)
df.sort_values(by=['Price'], inplace=True)


writer = pd.ExcelWriter("data.xlsx")
df.to_excel(writer, sheet_name='my_analysis', index=False, na_rep='NaN')

for column in df:
    column_width = max(df[column].astype(str).map(len).max(), len(column))
    col_idx = df.columns.get_loc(column)
    writer.sheets['my_analysis'].set_column(col_idx, col_idx, column_width)

writer.save()




