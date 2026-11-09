"""Configuración central de la suite."""
import os

BASE_URL = "https://www.saucedemo.com"
TIMEOUT = int(os.getenv("QA_TIMEOUT", "10"))       # espera explícita (s)
HEADLESS = os.getenv("QA_HEADLESS", "1") == "1"    # 0 para ver el navegador

USUARIO_VALIDO = "standard_user"
PASSWORD_VALIDO = "secret_sauce"
PASSWORD_INVALIDO = "clave_incorrecta"

EVIDENCIAS_DIR = os.path.join(os.path.dirname(__file__), "evidencias")
