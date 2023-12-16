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

    button_enter_system = driver.find_element(By.XPATH, '//*[@id="BtnOpen"]').click()
    time.sleep(1)

    # driver.switch_to.alert.dismiss() - Se incluye para eliminar mensajes de contraseña de navegador.
    # time.sleep(2)

    button_admin = driver.find_element(By.XPATH, '//*[@id="sidebar"]/div/div[4]/ul/li[2]/a').click()
    time.sleep(1)
    
    button_create = driver.find_element(By.XPATH, '//*[@id="AdminForm"]/li[1]/a').click()
    time.sleep(1)

    assert True

def test_associate_client():
    field_user_register = driver.find_element(By.XPATH, '//*[@id="main_body"]/div/div/main/div/div/div/div[2]/div[2]/div/div/div[2]/div/div[1]/input')
    field_user_register.send_keys("alex")
    time.sleep(1)

    button_search = driver.find_element(By.XPATH, '//*[@id="btnBuscar"]').click()
    time.sleep(3)

    check_client = driver.find_element(By.XPATH, '//*[@id="asociar"]').click()
    time.sleep(1)

    assert True

def test_create_user():
    field_user_register = driver.find_element(By.XPATH, '//*[@id="FormCrear"]/div/div[1]/input')
    field_user_register.send_keys("usuario1")
    time.sleep(1)
    
    field_pass_register = driver.find_element(By.XPATH, '//*[@id="password"]')
    field_pass_register.send_keys("123456+")
    time.sleep(1)
    
    field_pass_repeat = driver.find_element(By.XPATH, '//*[@id="password2"]')
    field_pass_repeat.send_keys("123456+")
    time.sleep(1)

    select_city = driver.find_element(By.XPATH, '//*[@id="ciudad"]').click()
    select_city = driver.find_element(By.XPATH, '//*[@id="ciudad"]/option[3]').click()
    time.sleep(1)
    
    check_state = driver.find_element(By.XPATH, '//*[@id="estado"]').click()
    time.sleep(1)

    button_create = driver.find_element(By.XPATH, '//*[@id="btnCrear"]').click()
    time.sleep(2)

    assert True

test_register()
time.sleep(2)
test_associate_client()
time.sleep(2)
test_create_user()
driver.quit()
