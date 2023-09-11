from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Configurar o serviço do ChromeDriver usando o ChromeDriverManager
servico = Service(ChromeDriverManager().install())

# Inicializar o navegador Chrome com o serviço configurado
navegador = webdriver.Chrome(service=servico)

# Abrir o site IMDb
navegador.get('https://www.imdb.com/')

# Esperar implicitamente por até 3 segundos
navegador.implicitly_wait(3)

# Encontrar o elemento com o ID 'imdbHeader' e extrair seu texto
dado1 = navegador.find_element(By.ID, 'imdbHeader').text

print('------------------')
print('Texto dentro do elemento com ID "imdbHeader": ', dado1)
print('------------------')

# Encontrar o elemento com a classe 'ipc-slate-card__content' e extrair seu texto
dado2 = navegador.find_element(By.CLASS_NAME, 'ipc-slate-card__content').text

print('-------------------')
print('Texto dentro do elemento com classe "ipc-slate-card__content": ', dado2)
print('-------------------')

# Encontrar o primeiro elemento com a tag 'h3' e extrair seu texto
nomeFill = navegador.find_element(By.TAG_NAME, 'h3').text

print('-------------------')
print('O primeiro título dentro do site é: ', nomeFill)
print('-------------------')

# Encontrar o campo de busca e enviar as teclas 'Breaking Bad'
campo_busca = navegador.find_element(By.NAME, 'q')
campo_busca.send_keys('House of Cards')

# Esperar implicitamente por mais 3 segundos após enviar as teclas
navegador.implicitly_wait(3)

print('-------------------')
print('Texto no campo de busca:', campo_busca.get_attribute('value'))
print('-------------------')
