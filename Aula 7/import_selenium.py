from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#driver2 = webdriver.Firefox(service=FirefoxService(executable_path=GeckoDriverManager().install()))
servico = ChromeService(ChromeDriverManager().install()) 
with webdriver.Chrome(service=servico) as driver:
    driver.get('https://pythonexamples.org/') 
    driver.find_element(By.LINK_TEXT, 'openCV').click
    driver.back()
    driver.refresh()
    driver.implicitly_wait(4)