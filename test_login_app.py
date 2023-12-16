# Se instala el driver de acuerdo con la versión del Chrome.
# https://googlechromelabs.github.io/chrome-for-testing/#stable
# Instalación del Driver (Solo se reemplaza el archivo): C:\driver_chrome

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path=r"C:\driver_chrome\chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get('http://localhost/MQ_Textil/');

def test_register():
    field_user_register = driver.find_element(By.XPATH, '//*[@id="LoginForm"]/div[1]/input')
    field_user_register.send_keys("jimmyco")
    time.sleep(1)
    
    field_pass_register = driver.find_element(By.XPATH, '//*[@id="LoginForm"]/div[2]/input')
    field_pass_register.send_keys("sophia")
    time.sleep(1)

    tokenApp = driver.find_element(By.XPATH, '//*[@id="token"]').get_attribute('value') # Control Temporal para Capturar Token.
    
    field_token_register = driver.find_element(By.XPATH, '//*[@id="codSeg"]')
    field_token_register.send_keys(tokenApp)
    time.sleep(2)

    button_recaptcha = driver.find_element(By.XPATH, '//*[@id="recaptcha-anchor"]/div[1]').click()
    time.sleep(10)

    button_enter_system = driver.find_element(By.XPATH, '//*[@id="BtnOpen"]').click()
    time.sleep(1)

    assert True

test_register()
driver.quit()
