#from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.common.by import By


#servico = Service(ChromeDriverManager().install())
#driver = webdriver.Chrome(service=servico) 

#driver.get('https://www.imdb.com/title/tt0120338/videogallery/')

#from selenium.webdriver.support.ui import Select

#elementSelect = Select(driver.find_element(By.NAME, 'sort'))
#elementSelect.select_by_value('expiration')

#driver.implicitly_wait(2)

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico) 

driver.get('file:///Z:/TI/DESENVOLVIMENTO%20DE%20SISTEMAS/IDSI/ALUNOS/Henrique%20Dourado/Back-End/Data%20Science%20e%20Data%20Analytics/Aula%2008/pagina_html_passo09.html')

driver.implicitly_wait(2)
time.sleep(3)
elementSelect = Select(driver.find_element(By.NAME, 'selectomatic'))
elementSelect.select_by_value('one')

valor_selecionado = elementSelect.first_selected_option.text
print("Valor selecionado 1:", valor_selecionado)

elementSelect = Select(driver.find_element(By.NAME, 'selectomatic'))
elementSelect.select_by_value('two')

valor_selecionado = elementSelect.first_selected_option.text
print("Valor selecionado 2:", valor_selecionado)

elementSelect = Select(driver.find_element(By.NAME, 'selectomatic'))
elementSelect.select_by_value('four')

valor_selecionado = elementSelect.first_selected_option.text
print("Valor selecionado 3:", valor_selecionado)

elementSelect = Select(driver.find_element(By.NAME, 'selectomatic'))
elementSelect.select_by_value('still learning how to count, apparently')


valor_selecionado = elementSelect.first_selected_option.text
print("Valor selecionado 4:", valor_selecionado)