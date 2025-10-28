from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/textinput")

Area_input = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
Area_input.send_keys("SkyPro")

blue_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()
print(driver.find_element(By.CSS_SELECTOR, "#updatingButton").text)

driver.quit()