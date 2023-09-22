from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import urllib.request
servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico) 

driver.get('https://www.ibm.com/br-pt/data-science?lnk=flatitem')

idImagens = driver.find_elements(By.CLASS_NAME, 'bx--image__img')[0]
atributoSRC = idImagens.get_attribute('src')
print(atributoSRC)

try:
    urllib.request.urlretrieve(atributoSRC,r'Z:\TI\DESENVOLVIMENTO DE SISTEMAS\IDSI\ALUNOS\Henrique Dourado\Back-End\Data Science e Data Analytics\Aula 08\image\ibm-image-selenium.jpg')
    print('Imagem Salva')
except:
    print('Ocorreu um erro e a Imagem não foi salva.')

