"""Clase base del Page Object Model: esperas explícitas y acciones comunes."""
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import TIMEOUT


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, TIMEOUT)

    def visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def clic(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def escribir(self, locator, texto):
        campo = self.visible(locator)
        campo.clear()
        if texto:
            campo.send_keys(texto)

    def texto(self, locator):
        return self.visible(locator).text
