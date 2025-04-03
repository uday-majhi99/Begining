from selenium import webdriver

# Initialize the browser
driver = webdriver.Chrome()

# Navigate to Google
driver.get("https://www.google.com")

# Keep the browser open for 5 seconds before closing
import time
time.sleep(5)

# Close the browser
driver.quit()
