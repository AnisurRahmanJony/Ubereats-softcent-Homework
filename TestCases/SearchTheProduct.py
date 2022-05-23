from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()

driver.get("https://www.ubereats.com/")

print(driver.title)

driver.find_element_by_css_selector("#location-typeahead-home-input").send_keys("Dhaka")
driver.find_element_by_xpath("1").click();