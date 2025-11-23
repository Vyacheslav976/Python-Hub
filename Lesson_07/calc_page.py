from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(5)
        self._driver.maximize_window()

    def set_delay(self, value_delay):

        self._driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self._driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(value_delay)

    def operation_calc(self, _button):

        self._driver.find_element(By.XPATH,"//span[text()='{_button}']").click()
        # self._driver.find_element(By.XPATH, "//span[text()='+']").click()
        # self._driver.find_element(By.XPATH, "//span[text()='8']").click()
        # self._driver.find_element(By.XPATH, "//span[text()='=']").click()

    def get_result(self):

        WebDriverWait(self._driver, 60).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))
        return self._driver.find_element(By.CSS_SELECTOR, ".screen").text