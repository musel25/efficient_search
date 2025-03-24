from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome options (optional: you can add a user profile to help avoid captchas)
options = webdriver.ChromeOptions()
# options.add_argument("user-data-dir=/path/to/your/chrome/profile")

# Initialize the driver using webdriver_manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open Google
driver.get("https://www.google.com")

# Locate the search box and perform a search
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("your search query")  # Replace with your search term
search_box.send_keys(Keys.RETURN)

# Wait for results to load (adjust the delay if needed)
time.sleep(5)

# If a captcha is encountered, let the user solve it manually
if "sorry" in driver.current_url:
    input("Captcha encountered. Please solve it in the browser, then press Enter to continue...")



for i in range(1, 21):
    dynamic_xpath = f'//*[@id="rso"]/div[{i}]/div/div/div[1]/div/div/span/a'
    try:
        element = driver.find_element(By.XPATH, dynamic_xpath)
        url = element.get_attribute("href")
        print(f"Opening result {i}: {url}")
        driver.execute_script("window.open(arguments[0]);", url)
    except Exception as e:
        print(f"Result at index {i} not found: {e}")


# Keep the browser open until you decide to close it
input("Press Enter to exit and close the browser...")
driver.quit()

