"""Page Object de la pantalla de login."""
from selenium.webdriver.common.by import By

from config import BASE_URL
from pages.base_page import BasePage


class LoginPage(BasePage):
    USUARIO = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    BOTON_LOGIN = (By.ID, "login-button")
    MENSAJE_ERROR = (By.CSS_SELECTOR, "[data-test='error']")

    def abrir_login(self):
        self.driver.get(BASE_URL)
        return self

    def iniciar_sesion(self, usuario, password):
        self.escribir(self.USUARIO, usuario)
        self.escribir(self.PASSWORD, password)
        self.clic(self.BOTON_LOGIN)
        return self

    def mensaje_error(self):
        return self.texto(self.MENSAJE_ERROR)
