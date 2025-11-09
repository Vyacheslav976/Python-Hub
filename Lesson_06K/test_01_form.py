from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()

def test_input_form():
    try:
        waiter = WebDriverWait(driver, 40)

        driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

        driver.find_element(By.NAME, "first-name").send_keys("Иван")
        driver.find_element(By.NAME, "last-name").send_keys("Петров")
        driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        driver.find_element(By.NAME, "zip-code").send_keys("")
        driver.find_element(By.NAME, "city").send_keys("Москва")
        driver.find_element(By.NAME, "country").send_keys("Россия")
        driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
        driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
        driver.find_element(By.NAME, "job-position").send_keys("QA")
        driver.find_element(By.NAME, "company").send_keys("SkyPro")

        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        waiter.until(EC.visibility_of_element_located((By.ID, "zip-code")))

        zip_code_field = driver.find_element(By.ID, "zip-code").value_of_css_property("background-color")

        assert zip_code_field == "rgba(248, 215, 218, 1)", f"Поле {zip_code_field} не подсвечено красным"

        fields = ["first-name", "last-name", "address", "city", "country", "e-mail", "phone", "job-position", "company"]

        for field in fields:
            color_field = driver.find_element(By.ID, field).value_of_css_property("background-color")

            assert color_field == "rgba(209, 231, 221, 1)", f"Поле {color_field} не подсвечено зеленым"
    finally:
        driver.quit()
