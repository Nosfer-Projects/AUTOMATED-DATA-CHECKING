from selenium.webdriver.chrome.service import Service
from modules.x_com import Xkom
from modules.data_excel import DataExcel

chrome_driver_path = Service("D:/PROGRAMOWANIE/Chrome driver/chromedriver.exe")

if __name__=='__main__':
    price_pc = int(input("How much can you spend on buying a new gaming computer? Please enter the amount in the currency PLN : "))
    new_pc = Xkom(chrome_driver_path, price_pc)
    new_pc.find_pc()
    list_of_pcs=new_pc.web_data()
    DataExcel.create_data(list_of_pcs)






