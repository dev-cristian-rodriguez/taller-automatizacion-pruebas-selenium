# Taller: automatización de pruebas con Selenium

Asignatura: Pruebas y Calidad del Software, Universidad Tecnológica del Oriente.
Estudiante: Cristian Estiven Rodriguez Benitez.

Suite de pruebas funcionales con Selenium WebDriver, Python y pytest (patrón Page Object Model) sobre https://www.saucedemo.com: login, carrito y checkout.

## Instalación

```bash
python3 -m venv .venv
source .venv/bin/activate          # En Windows: .venv\Scripts\activate
pip install -r requirements.txt    # requiere Google Chrome instalado
```

## Ejecución

```bash
pytest                    # toda la suite (headless)
pytest -m happy           # solo caminos felices
pytest -m negative        # solo manejo de errores
QA_HEADLESS=0 pytest      # con el navegador visible
```

Las capturas quedan en `evidencias/` y el reporte HTML en `reportes/`.
