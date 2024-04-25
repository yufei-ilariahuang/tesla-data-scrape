# Extract title
    # title = driver.find_element(By.CSS_SELECTOR, 'h1').text

    # # Find all links and corresponding addresses
    # locations = driver.find_elements(By.CSS_SELECTOR, 'a[href*="/findus/location/supercharger"]')
    # addresses = driver.find_elements(By.CSS_SELECTOR, '.street-address-states')

    # # Print the extracted information
    # print(title)
    # for location, address in zip(locations, addresses):
    #     print(f"Location: {location.text}, URL: {location.get_attribute('href')}")
    #     print(f"Address: {address.text}")