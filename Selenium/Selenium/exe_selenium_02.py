from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
from selenium.webdriver.common.by import By

navegador.get('https://statusinvest.com.br/fundos-imobiliarios/knri11')

navegador.implicitly_wait(3)

dado0 = navegador.find_element(By.CLASS_NAME,'value').text
dado1 = navegador.find_elements(By.CLASS_NAME, 'value')[0].text
dado2 = navegador.find_elements(By.CLASS_NAME, 'value')[1].text
dado3 = navegador.find_elements(By.CLASS_NAME, 'value')[2].text
dado4 = navegador.find_elements(By.CLASS_NAME, 'value')[3].text

print(dado0)
print(dado1)
print(dado2)
print(dado3)
print(dado4)