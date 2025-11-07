from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

def test_form_validation():

     try:
        driver.get("https://www.saucedemo.com")

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))

        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

        driver.execute_script("window.scrollTo(0, 500)")

        cart_badge = driver.find_element(By.CSS_SELECTOR, "span.shopping_cart_badge").text
        assert int(cart_badge) == 3

        driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()

        WebDriverWait(driver, 10).until(
             EC.presence_of_element_located((By.ID, "item_4_title_link")))
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "item_1_title_link")))
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "item_2_title_link")))

        driver.find_element(By.ID, "checkout").click()

        WebDriverWait(driver, 10).until(
             EC.presence_of_element_located((By.ID, "first-name")))

        driver.find_element(By.ID, "first-name").send_keys("Vyacheslav")
        driver.find_element(By.ID, "last-name").send_keys("Vokov")
        driver.find_element(By.ID, "postal-code").send_keys("390048")
        driver.find_element(By.ID, "continue").click()

        WebDriverWait(driver, 15).until(
             EC.presence_of_element_located((By.CLASS_NAME, "div.summary_total_label")))

        total_text = driver.find_element(By.CLASS_NAME, "div.summary_total_label").text

        total_value = total_text[-5:]

        assert float(total_value) == 58.29

     finally:
        driver.quit()