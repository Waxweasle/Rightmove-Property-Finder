from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import smtplib


GOOGLE_FORM = "FORM LINK HERE"
RENTAL_PROPERTIES = "YOUR RIGHTMOVE SEARCH LINK HERE"
DRIVER_PATH = "YOUR DRIVER PATH HERE"
options = Options()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")


class PropertyFinder:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(DRIVER_PATH), options=options)

    def get_properties(self):
        self.driver.get(RENTAL_PROPERTIES)
        self.properties = self.driver.find_elements(By.ID, value="l-searchResults")

    def property_data(self):
        # GET PROPERTY ADDRESS
        self.page_address = self.driver.find_elements(By.CLASS_NAME, value="propertyCard-address")
        self.address_list = [x.text for x in self.page_address]
        print(self.address_list)

        # GET PROPERTY PRICE
        self.page_prices = self.driver.find_elements(By.CLASS_NAME, value="propertyCard-priceLink")
        self.prices_list = [x.text for x in self.page_prices]
        self.prices_list_clean = [x.replace("\n", ' ') for x in self.prices_list]
        print(self.prices_list_clean)

        # GET PROPERTY LINK
        self.links_in_page = self.driver.find_elements(By.CLASS_NAME, value="propertyCard-link ")
        self.links_list = [x.get_attribute("href") for x in self.links_in_page]
        print(self.links_list)

    # FILLS OUT GOOGLE FORM - RESULTS ENTERED TO GOOGLE SHEET FOR EASY ACCESS & READABILITY
    def fill_form(self):
        self.driver.get(GOOGLE_FORM)
        time.sleep(3)
        total = len(self.prices_list_clean)
        while True:
            for x in range(len(self.prices_list_clean)):
                self.fields = self.driver.find_elements(By.CLASS_NAME, value="whsOnd")
                fill_address = self.fields[0]
                fill_address.send_keys(self.address_list[x])
                fill_price = self.fields[1]
                fill_price.send_keys(self.prices_list_clean[x])
                fill_link = self.fields[2]
                fill_link.send_keys(self.links_list[x])
                # SUBMIT
                self.driver.find_element(By.CLASS_NAME, value="uArJ5e").click()
                self.driver.get(GOOGLE_FORM)
                time.sleep(3)
                total -= 1
            if total == 0:
                print("All properties added.")
                break


def send_email():
    me = "YOUR EMAIL HERE"
    pw = "YOUR PASSWORD HERE"
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
        connection.starttls()
        connection.login(user=me, password=pw)
        connection.sendmail(from_addr=me,
                            to_addrs="TARGET EMAIL HERE",
                            msg=f"You have new properties available to view! \n\n {message}".encode('utf-8'))


message = "New properties have been found that match your search criteria on Rightmove! Check out your Sheety file to" \
          "view them."
finder = PropertyFinder()
finder.get_properties()
finder.property_data()
finder.fill_form()
send_email()

