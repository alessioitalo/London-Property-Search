from bs4 import BeautifulSoup
import requests
from selenium import webdriver

GFORM = "YOUR GOOGLE FORM"
LINK = "https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=REGION%5E92830&maxBedrooms=1&minBedrooms=1&maxPrice=1400&minPrice=1200&propertyTypes=&mustHave=&dontShow=houseShare&furnishTypes=&keywords="
CHROME_DRIVER = "YOUR EXECUTABLE CHROME DRIVER"


response = requests.get(LINK)
soup = BeautifulSoup(response.text, "html.parser")

addresses = soup.findAll(name="address", class_="propertyCard-address")
addresses_list = [address.getText().strip('\n') for address in addresses]
prices = soup.findAll(name="span", class_="propertyCard-priceValue")
prices_list = [price.getText() for price in prices]
links = soup.findAll(name="a", class_="propertyCard-link")
links_list = [f"https://www.rightmove.co.uk{link.get('href')}" for link in links[::2]]

for i in range(len(addresses_list)):
    driver = webdriver.Chrome(CHROME_DRIVER)
    driver.get(GFORM)
    form_address = driver.find_element_by_css_selector("#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(1) > div > div > div.freebirdFormviewerComponentsQuestionTextRoot > div > div.quantumWizTextinputPaperinputMainContent.exportContent > div > div.quantumWizTextinputPaperinputInputArea > input")
    form_price = driver.find_element_by_css_selector("#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(2) > div > div > div.freebirdFormviewerComponentsQuestionTextRoot > div > div.quantumWizTextinputPaperinputMainContent.exportContent > div > div.quantumWizTextinputPaperinputInputArea > input")
    form_link = driver.find_element_by_css_selector("#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(3) > div > div > div.freebirdFormviewerComponentsQuestionTextRoot > div > div.quantumWizTextinputPaperinputMainContent.exportContent > div > div.quantumWizTextinputPaperinputInputArea > input")
    button_submit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    form_address.send_keys(addresses_list[i])
    form_price.send_keys(prices_list[i])
    form_link.send_keys(links_list[i])
    button_submit.click()
    driver.quit()

