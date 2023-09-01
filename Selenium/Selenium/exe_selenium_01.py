from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
from selenium.webdriver.common.by import By

navegador.get('https://www.infomoney.com.br/')
navegador.implicitly_wait(3)

dado1 = navegador.find_element(By.ID, 'high').text
dado2 = navegador.find_elements(By.ID, 'high')[0].text

print('------------------')
print(dado1)
print('------------------')
print(dado2)
print('------------------')