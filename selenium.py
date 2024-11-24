from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver (this example uses Chrome)
driver = webdriver.Chrome(executable_path='pathtochromedriver')  # Replace with your path to chromedriver

# Open a website (e.g., Google)
driver.get(httpswww.google.com)

# Ensure the page has loaded
time.sleep(2)

# Find the search input field (use the name attribute of the input element)
search_box = driver.find_element(name, q)

# Type a search query into the search box and submit
search_box.send_keys(Selenium automation)
search_box.send_keys(Keys.RETURN)

# Wait for the results to load
time.sleep(3)

# Take a screenshot of the results page
driver.save_screenshot(search_results.png)

# Close the browser
driver.quit()
