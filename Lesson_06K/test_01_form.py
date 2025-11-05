import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# edge_driver_path = r"C:\Users\alexa\Desktop\Обучение\06 Автоматизация Python\edgedriver_win64\msedgedriver.exe"
driver = webdriver.Edge(service=EdgeService(edge_driver_path))

def test_input_form():

    # try:
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        waiter = WebDriverWait(driver, 40)

    driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

    waiter.until(EC.visibility_of_element_located(By.ID, "#zip-code"))

    first_name = driver.find_element(By.NAME, "first-name").send_keys("Иван")
    last_name = driver.find_element(By.NAME, "last-name").send_keys("Петров")
    address = driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    zip_code = driver.find_element(By.NAME, "zip-code").send_keys("")
    city = driver.find_element(By.NAME, "city").send_keys("Москва")
    country = driver.find_element(By.NAME, "country").send_keys("Россия")
    email = driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    phone_number = driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    job_position = driver.find_element(By.NAME, "job-position").send_keys("QA")
    company = driver.find_element(By.NAME, "company").send_keys("SkyPro")

    submit = driver.find_element(By.XPATH, "button[type='submit']").click()

    zip_code_field = driver.find_element(By.ID, "zip-code").value_of_css_property("background-color")

    # assert  zip_code_field == "rgb(248, 215, 218)", f"Поле {zip_code_field} не подсвечено красным"
    assert setup.get_zip_code_field() == "rgb(248, 215, 218), f'Поле {zip_code_field} не подсвечено красным'"
    fields = ["first_name", "last_name", "address", "city", "country", "email", "phone_number", "job_position", "company"]

    for field in fields:
        field = driver.find_elements(By.ID, field).value_of_css_property("background-color")
    # assert field == "rgb(209, 231, 221)", f"Поле {field} не подсвечено зеленым"
    assert setup.get_field() == "rgb(248, 215, 218)", f"Поле {field} не подсвечено зеленым"

    driver.quit()




