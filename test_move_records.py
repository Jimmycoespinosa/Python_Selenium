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

    button_operation = driver.find_element(By.XPATH, '//*[@id="sidebar"]/div/div[4]/ul/li[3]/a').click()
    time.sleep(1)
    
    button_apps = driver.find_element(By.XPATH, '//*[@id="AdminForm"]/li[1]/a').click()
    time.sleep(1)

    assert True

def test_move_table():
    button_move = driver.find_element(By.XPATH, '//*[@id="main_body"]/div/div/main/div/div/div/div[2]/div/div/div[2]/div/div/div/nav/ul/li[2]/a').click()
    time.sleep(1)

    button_move_one = driver.find_element(By.XPATH, '//*[@id="main_body"]/div/div/main/div/div/div/div[2]/div/div/div[2]/div/div/div/nav/ul/li[3]/a').click()
    time.sleep(1)

    button_move_two = driver.find_element(By.XPATH, '//*[@id="main_body"]/div/div/main/div/div/div/div[2]/div/div/div[2]/div/div/div/nav/ul/li[4]/a').click()
    time.sleep(1)

    assert True

test_register()
time.sleep(2)
test_move_table()
driver.quit()
