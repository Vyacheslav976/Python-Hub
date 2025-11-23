from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/dynamicid")

dinamic_blu_button = "//button[text()='Button with Dynamic ID']"
search_blu_button = driver.find_element(By.XPATH, dinamic_blu_button)
search_blu_button.click()

sleep(5)

driver.quit()