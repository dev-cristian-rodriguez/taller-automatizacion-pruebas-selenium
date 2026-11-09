"""Page Objects del catálogo, el carrito y el checkout."""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class InventoryPage(BasePage):
    TITULO = (By.CSS_SELECTOR, "[data-test='title']")
    ITEMS = (By.CSS_SELECTOR, "[data-test='inventory-item']")
    AGREGAR_MOCHILA = (By.ID, "add-to-cart-sauce-labs-backpack")
    BADGE = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
    CARRITO = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")

    def titulo(self):
        return self.texto(self.TITULO)

    def cantidad_productos(self):
        self.visible(self.ITEMS)
        return len(self.driver.find_elements(*self.ITEMS))

    def agregar_mochila(self):
        self.clic(self.AGREGAR_MOCHILA)
        return self

    def items_en_carrito(self):
        return int(self.texto(self.BADGE))

    def ir_al_carrito(self):
        self.clic(self.CARRITO)


class CartPage(BasePage):
    NOMBRES = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    CHECKOUT = (By.ID, "checkout")

    def nombres_items(self):
        self.visible((By.CSS_SELECTOR, "[data-test='title']"))
        return [e.text for e in self.driver.find_elements(*self.NOMBRES)]

    def iniciar_checkout(self):
        self.clic(self.CHECKOUT)


class CheckoutPage(BasePage):
    NOMBRE = (By.ID, "first-name")
    APELLIDO = (By.ID, "last-name")
    POSTAL = (By.ID, "postal-code")
    CONTINUAR = (By.ID, "continue")
    FINALIZAR = (By.ID, "finish")
    TOTAL = (By.CSS_SELECTOR, "[data-test='total-label']")
    EXITO = (By.CSS_SELECTOR, "[data-test='complete-header']")

    def completar_datos(self, nombre, apellido, postal):
        self.escribir(self.NOMBRE, nombre)
        self.escribir(self.APELLIDO, apellido)
        self.escribir(self.POSTAL, postal)
        self.clic(self.CONTINUAR)
        return self

    def total(self):
        return self.texto(self.TOTAL)

    def finalizar(self):
        self.clic(self.FINALIZAR)
        return self

    def mensaje_exito(self):
        return self.texto(self.EXITO)
