from time import sleep
from selenium import webdriver
#from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr")

locator_blu_button = ".btn.class3.btn-primary.btn-test"
search_blu_button = driver.find_element(By.CSS_SELECTOR, locator_blu_button)
search_blu_button.click()

sleep(5)

driver.quit()