from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set up the driver (make sure you have the correct path to your WebDriver, e.g., ChromeDriver)
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

# Open Google
driver.get("https://www.google.com")

# Find the search box (Google uses the name "q" for its search input)
search_box = driver.find_element("name", "q")
search_box.send_keys("your search query")  # Replace with your desired search query
search_box.send_keys(Keys.RETURN)

# Wait a moment for the results to load
time.sleep(2)

# Grab the first 10 search result links.
# Note: Google's page structure may change over time. Currently, the search results are under a div with class "yuRUbf".
results = driver.find_elements("xpath", '//div[@class="yuRUbf"]/a')

# Open each of the first 10 results in a new tab
for result in results[:10]:
    url = result.get_attribute("href")
    driver.execute_script("window.open(arguments[0]);", url)

# Optionally, you might want to switch focus or add further automation here.
