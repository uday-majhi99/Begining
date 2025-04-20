from appium import webdriver
import time

desired_caps = {
    "platformName": "Android",
    "deviceName": "Android Emulator",  # or actual device ID
    "appPackage": "com.example.myapplication",  # your app's package
    "appActivity": "com.example.myapplication.MainActivity",  # your app's main activity
    "automationName": "UiAutomator2"
}

# Connect to Appium server
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities=desired_caps)


# Wait a few seconds to see the app launch
time.sleep(5)

# Close the app and end session
driver.quit()
