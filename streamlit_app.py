import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Configuración del navegador
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Inicializar navegador con Selenium
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# URL del broker (ejemplo: Olymp Trade)
broker_url = 'https://www.olymptrade.com'

def iniciar_sesion(usuario, contrasena):
    driver.get(broker_url)
    time.sleep(5)  # Esperar a que la página cargue
    
    # Buscar e ingresar usuario
    driver.find_element(By.NAME, 'email').send_keys(usuario)
    
    # Buscar e ingresar contraseña
    driver.find_element(By.NAME, 'password').send_keys(contrasena)
    driver.find_element(By.NAME, 'password').send_keys(Keys.RETURN)
    time.sleep(5)
    
    print("Sesión iniciada con éxito")

def verificar_saldo():
    time.sleep(3)
    try:
        saldo = driver.find_element(By.CLASS_NAME, 'balance-amount').text
        print(f"Saldo disponible: {saldo}")
    except Exception as e:
        print(f"Error al verificar saldo: {e}")

def cerrar_navegador():
    driver.quit()

# Ejecución del bot
if __name__ == '__main__':
    usuario = 'tu_correo@ejemplo.com'
    contrasena = 'tu_contraseña'
    
    try:
        iniciar_sesion(usuario, contrasena)
        verificar_saldo()
    except Exception as e:
        print(f"Error durante la ejecución: {e}")
    finally:
        cerrar_navegador()
