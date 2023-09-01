from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
from selenium.webdriver.common.by import By

navegador.get('https://www.imdb.com/')

navegador.implicitly_wait(3)

campo_busca = navegador.find_elements(By.NAME, 'q')[0]
campo_busca.send_keys('Breaking Bad')
navegador.implicitly_wait(3)