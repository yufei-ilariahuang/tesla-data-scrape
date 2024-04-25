import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
def try_scrape_tesla_all():
    # Wait for the page to load completely
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    driver = webdriver.Chrome(options=options)

    # Go to the Tesla supercharger page for Morocco
    driver.get('https://www.tesla.com/findus/list/stores/Belgium')
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h1')))
        print("Page loaded successfully.")
    except TimeoutError:
        print("Page load timed out.")

    # Extract title
    titles = driver.find_element_by_xpath('/html/body/section/div/div/header/h1')

    # Find all links and corresponding addresses
    locations = driver.find_elements(By.CSS_SELECTOR, 'a[href*="/findus/location"]')
    addresses = driver.find_elements(By.CSS_SELECTOR, '.street-address-states')
    postals = driver.find_elements(By.CSS_SELECTOR, '.locality-city-postal')

    # Store the extracted information in a list of dictionaries
    sample = [{"title": titles.text}]

    for location, address, postal in zip(locations, addresses, postals):
        sample_info = {
            "location": location.text,
            "url": location.get_attribute('href'),
            "address": address.text,
            "postal": postal.text
        }
        sample.append(sample_info)

    with open('tesla_sample.json', 'w') as f:
        json.dump(sample, f, indent=4)
        
    driver.quit()

def try_scrape_tesla_superchargers():
    # Set up the Chrome WebDriver
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    driver = webdriver.Chrome(options=options)

    # Go to the Tesla supercharger page for Morocco
    driver.get('https://www.tesla.com/findus/list/superchargers/Morocco')

    # Wait for the page to load completely
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h1')))
        print("Page loaded successfully.")
    except TimeoutError:
        print("Page load timed out.")

    # Extract title
  
    titles = driver.find_element_by_xpath('/html/body/section/div/div/header/h1')
    # Find all links and corresponding addresses
    locations = driver.find_elements(By.CSS_SELECTOR, 'a[href*="/findus/location/supercharger"]')
    addresses = driver.find_elements(By.CSS_SELECTOR, '.street-address-states')
    postals = driver.find_elements(By.CSS_SELECTOR, '.locality-city-postal')

    # Store the extracted information in a dictionary
    superchargers = [{"title": titles.text}]

    for location, address, postal in zip(locations, addresses, postals):
        supercharger_info = {
            "location": location.text,
            "url": location.get_attribute('href'),
            "address": address.text,
            "postal": postal.text
        }
        superchargers.append(supercharger_info)

    # Write the data to a JSON file
    with open('tesla_superchargers.json', 'w') as f:
        json.dump(superchargers, f, indent=4)

    #Clean up
    driver.quit()
    
    
def try_scrape_tesla_locations():
    # Set up the Chrome WebDriver
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    driver = webdriver.Chrome(options=options)
    
    # Open the main page
    driver.get('https://www.tesla.com/findus/list')
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h1')))
        print("Page loaded successfully.")
    except TimeoutError:
        print("Page load timed out.")

    # Find all the locations' links
    all_links = driver.find_elements(By.XPATH, '//a')
    base_url = 'https://www.tesla.com/findus/list/'
    desired_links = []
    for link in all_links:
        if base_url in link.get_attribute('href'):
            desired_links.append(link.get_attribute('href'))
    for link in desired_links:
        print(link)
    # # Iterate through each location link
   
    driver.quit()
    
# if __name__ == "__main__":
# #     scrape_and_write_to_json()
#     try_scrape_tesla_all()
