#python -m Venv env -- Create virtual environment
# .\env\Scripts\activate -- Activate environment

from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import pandas as pd

class WebScrappy:

    def __init__(self):
        chrome_options = Options()
        chrome_options.headless =False
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\henri\Anaconda3\chromedriver.exe', options=chrome_options)
        self.driver.set_window_size(800,700)
        

    def start(self):
        self.access_site()
    
    def access_site(self):
        # load the webpage
        self.driver.get('https://www.amazon.in/')
        # get the input elements
        input_search = self.driver.find_element_by_id('twotabsearchtextbox')
        search_button = self.driver.find_element_by_xpath("(//input[@type='submit'])[1]")
        # send the input to the webpage
        input_search.send_keys("Machine Learning")
        sleep(1)
        search_button.click()
        self.extract_info()


    def extract_info(self):
        # create lists of product and price
        products_list = []
        prices_list = []
        
        for i in range(6):
            # get xpath
            print("Page: ", i+1)
            product = self.driver.find_elements_by_xpath('//span[@class = "a-size-medium a-color-base a-text-normal"]')
            Prices = self.driver.find_elements_by_xpath('//span[@class = "a-price-whole"]')
            # get values and insert in a list
            for p in range(len(product)):
                title = product[p].text
                price = Prices[p].text
                products_list.append(title)
                prices_list.append(price)
                
            
	    # next page
            next_page = self.driver.find_element_by_xpath("//li[@class='a-last']")
            next_page.click()
            sleep(2)
            
        self.save_info_excel(products_list, prices_list)

    def save_info_excel(self, products_list, prices_list):
        df = pd.DataFrame(columns=['Product'])
        for item in range(0, len(products_list)):
            df = df.append({'Product':
                products_list[item],
                'Price':
                prices_list[item],
            },ignore_index=True)

        df.to_excel('Worksheet.xlsx')
        print("Worksheet created successfully!")
        


scrappy = WebScrappy()
scrappy.start()

