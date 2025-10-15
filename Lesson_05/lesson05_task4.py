from time import sleep
from selenium import webdriver
from selenium.webdriver.Firefox.service import Service as FirefoxService
from webdriver_manager.Firefox import FirefoxDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox(service=FirefoxService(FirefoxDriverManager().install()))
#driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")

search_user_name = "input#username"
search_user_name = driver.find_element(By.CSS_SELECTOR, search_user_name)
search_user_name.send_keys("tomsmith")

search_password = "input#password"
search_password = driver.find_element(By.CSS_SELECTOR, search_password)
search_password.send_keys("SuperSecretPassword!")

search_Login_button = "i.fa.fa-2x.fa-sign-in"
search_Login_button = driver.find_element(By.CSS_SELECTOR, search_Login_button)
search_Login_button.click()

text_green_plashka = "div#flash"
text_green_plashka = driver.find_element(By.CSS_SELECTOR,"div#flash").text

print(text_green_plashka)


sleep(5)

driver.quit()