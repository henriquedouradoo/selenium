from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico) 

driver.get ('https://www.bibliaonline.com.br/acf/ex')
time.sleep

driver.execute_script('window.scrollTo(0, window.innerHeight);')

time.sleep(3)

driver.execute_script('window.scrollTo(0,0);')
time.sleep(3)
time.sleep(3)

driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
time.sleep(3)