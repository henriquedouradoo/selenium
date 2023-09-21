from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico) 

driver.get('file:///C:/Users/Aluno/Documents/Selenium/pagina_html_passo09.html')

driver.implicitly_wait(2)

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
