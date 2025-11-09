from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
def test_calc():
    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        driver.find_element(By.CSS_SELECTOR,"#delay").clear()
        driver.find_element(By.CSS_SELECTOR,"#delay").send_keys("45")
        driver.find_element(By.XPATH,"//span[text()='7']").click()
        driver.find_element(By.XPATH,"//span[text()='+']").click()
        driver.find_element(By.XPATH,"//span[text()='8']").click()
        driver.find_element(By.XPATH,"//span[text()='=']").click()

        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".screen")))
        WebDriverWait(driver, 60).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

        value = driver.find_element(By.CSS_SELECTOR, ".screen").text

        assert int(value) == 15
    finally:
        driver.quit()
