# Web Scraping E-commerce using Selenium

## Objetive

Extracting information from an ecommerce site with Selenium and download the information in excel file.

In this project extraction information (book title and price) in amazon site (in a legal way, of course) to create
my own database, because not always the data that we need are available in a structured way on the internet. Above all,
learning to have with the web scraping tools is very useful.

## Tools used

- Selenium
- Time
- pandas


## Implementation

First, import our libraries:

          from selenium import webdriver
          from time import sleep
          from selenium.webdriver.chrome.options import Options
          import pandas as 
          
  Then I created a class called WebScrappy. In the fuction __init__ we have Chrome WebDriver Options with my customize and configure a ChromeDriver session.
  
        def __init__(self):
              chrome_options = Options()
              chrome_options.headless =False
              chrome_options.add_experimental_option("detach", True)
              self.driver = webdriver.Chrome(executable_path=r'C:\Users\chromedriver.exe', options=chrome_options)
              self.driver.set_window_size(800,700)
        
I created one fuction to access the site.
        
        def start(self):
              self.access_site()
  
 Inside the access site fuction there are load the webpage, get the input elemens by xpath, send the input to the webpage with name Machine Learning,
 click on search button and call the extrac information fuction.
 
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

In extraction information fuction there are

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
        
  In the las funtion, we save the information on excel file

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
        
   Now we can instantiate our class with commands:
   
             crappy = WebScrappy()
             scrappy.start()
