from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico) 

driver.get('https://www.imdb.com/title/tt0120338/videogallery/')

from selenium.webdriver.support.ui import Select

elementSelect = Select(driver.find_element(By.NAME, 'sort'))
elementSelect.select_by_value('expiration')

driver.implicitly_wait(2)