from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set the path to the ChromeDriver
driver = webdriver.Chrome()

driver.maximize_window()

# Open Google
driver.get("https://www.google.com")

# Optional: Wait for a few seconds to see the page
time.sleep(5)

# Close the browser
driver.quit()