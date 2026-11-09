"""Fixtures: navegador limpio por prueba y captura de evidencia."""
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import config
from pages.login_page import LoginPage
from pages.shop_pages import InventoryPage


@pytest.fixture
def driver(request):
    opciones = Options()
    if config.HEADLESS:
        opciones.add_argument("--headless=new")
    opciones.add_argument("--window-size=1366,900")
    opciones.add_argument("--no-sandbox")
    # Evita el aviso de "contraseña filtrada" de Chrome, ajeno a la aplicación
    opciones.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
    })
    drv = webdriver.Chrome(options=opciones)
    yield drv
    # Una captura final por prueba, nombrada con la prueba y su resultado
    os.makedirs(config.EVIDENCIAS_DIR, exist_ok=True)
    rep = request.node.rep_call
    resultado = "FALLO" if rep.failed else ("DEFECTO" if rep.skipped else "OK")
    drv.save_screenshot(os.path.join(
        config.EVIDENCIAS_DIR, f"{request.node.name}_{resultado}.png"))
    drv.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    setattr(item, "rep_" + call.when, outcome.get_result())


@pytest.fixture
def login_page(driver):
    return LoginPage(driver).abrir_login()


@pytest.fixture
def sesion_iniciada(driver, login_page):
    login_page.iniciar_sesion(config.USUARIO_VALIDO, config.PASSWORD_VALIDO)
    return InventoryPage(driver)
