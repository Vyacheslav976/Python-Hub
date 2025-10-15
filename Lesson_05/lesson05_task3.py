from time import sleep
from selenium import webdriver
from selenium.webdriver.Firefox.service import Service as FirefoxService
from webdriver_manager.Firefox import FirefoxDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox(service=FirefoxService(FirefoxDriverManager().install()))
#driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")

search_input = "input"
search_input = driver.find_element(By.CSS_SELECTOR, search_input)
search_input.send_keys("Sky")
search_input.clear()
search_input.send_keys("Pro")


sleep(5)

driver.quit()