"""Pruebas funcionales de SauceDemo: login, carrito y checkout."""
import pytest

import config
from pages.shop_pages import CartPage, CheckoutPage


@pytest.mark.happy
def test_login_exitoso(driver, login_page, sesion_iniciada):
    assert "/inventory.html" in driver.current_url
    assert sesion_iniciada.titulo() == "Products"
    assert sesion_iniciada.cantidad_productos() == 6


@pytest.mark.negative
def test_login_credenciales_erroneas(driver, login_page):
    login_page.iniciar_sesion(config.USUARIO_VALIDO, config.PASSWORD_INVALIDO)
    assert "Username and password do not match" in login_page.mensaje_error()
    assert "/inventory.html" not in driver.current_url


@pytest.mark.negative
@pytest.mark.parametrize("usuario,password,esperado", [
    ("", config.PASSWORD_VALIDO, "Username is required"),
    (config.USUARIO_VALIDO, "", "Password is required"),
], ids=["usuario_vacio", "password_vacio"])
def test_login_campos_vacios(login_page, usuario, password, esperado):
    login_page.iniciar_sesion(usuario, password)
    assert esperado in login_page.mensaje_error()


@pytest.mark.happy
def test_agregar_producto_al_carrito(driver, sesion_iniciada):
    sesion_iniciada.agregar_mochila()
    assert sesion_iniciada.items_en_carrito() == 1
    sesion_iniciada.ir_al_carrito()
    assert CartPage(driver).nombres_items() == ["Sauce Labs Backpack"]


@pytest.mark.happy
def test_compra_completa(driver, sesion_iniciada):
    sesion_iniciada.agregar_mochila().ir_al_carrito()
    CartPage(driver).iniciar_checkout()
    checkout = CheckoutPage(driver).completar_datos("Cristian", "Rodriguez", "110111")
    assert "$32.39" in checkout.total()          # 29.99 + impuesto 2.40
    checkout.finalizar()
    assert checkout.mensaje_exito() == "Thank you for your order!"


@pytest.mark.negative
@pytest.mark.xfail(strict=True, reason="DEF-01: la app permite checkout con carrito vacío")
def test_checkout_con_carrito_vacio(driver, sesion_iniciada):
    """Regla de negocio: no debería poder iniciarse el checkout sin productos."""
    sesion_iniciada.ir_al_carrito()
    CartPage(driver).iniciar_checkout()
    assert "checkout-step-one" not in driver.current_url
