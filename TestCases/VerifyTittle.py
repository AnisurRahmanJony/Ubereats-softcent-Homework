from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()

driver.get("https://www.ubereats.com/")

ActualTittle  = driver.title
ExpectedTittle = "Uber Eats US | Food Delivery and Takeout | Order Online from Restaurants Near You"
print(ActualTittle)