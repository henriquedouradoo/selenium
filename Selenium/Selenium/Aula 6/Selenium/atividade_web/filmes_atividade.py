from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


servico = Service(ChromeDriverManager().install())


navegador = webdriver.Chrome(service=servico)


navegador.get('https://www.imdb.com/')


navegador.implicitly_wait(3)


dado1 = navegador.find_element(By.ID, 'imdbHeader').text

print('------------------')
print('Texto dentro do elemento com ID "imdbHeader": ', dado1)
print('------------------')


dado2 = navegador.find_element(By.CLASS_NAME, 'ipc-slate-card__content').text

print('-------------------')
print('Texto dentro do elemento com classe "ipc-slate-card__content": ', dado2)
print('-------------------')


nomeFill = navegador.find_element(By.TAG_NAME, 'h3').text

print('-------------------')
print('O primeiro título dentro do site é: ', nomeFill)
print('-------------------')


campo_busca = navegador.find_element(By.NAME, 'q')
campo_busca.send_keys('House of Cards')


navegador.implicitly_wait(3)

print('-------------------')
print('Texto no campo de busca:', campo_busca.get_attribute('value'))
print('-------------------')