from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
from selenium.webdriver.common.by import By

navegador.get('https://statusinvest.com.br/fundos-imobiliarios/knri11')

navegador.implicitly_wait(3)

nomeFill = navegador.find_elements(By.TAG_NAME, 'h1')[0].text
valorAtual = navegador.find_elements(By.TAG_NAME , 'strong')[0].text
tableRendimentos = navegador.find_elements(By.TAG_NAME, 'table')[0].text
tableResultados = navegador.find_elements(By.TAG_NAME, 'button')[0].text

print(nomeFill)
print(valorAtual)
print(tableRendimentos)
print(tableResultados)