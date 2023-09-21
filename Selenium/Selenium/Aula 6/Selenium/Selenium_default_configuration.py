#Importar o webdriver da Biblioteca SELENIUM

from selenium import webdriver

#Dentro do Webdriver, temos o WEBDRIVER_MANAGER, que usaremos para informar QUAL SERÁ O NAVEGADOR UTILIZADO (Podemos escolher entre o Firefox e o Chrome. Em nossas aulas, usaremos io navegador do Google)

from webdriver_manager.chrome import ChromeDriverMenager

#Como usaremos diverso recursos dentro do navegador,temos que habilitar alguns serviços. Portanto, vamos habilitar a função SERVICES do WEBDRIVER

from selenium.webdriver.chrome.service import Service

#Ao importarmos a FUNÇÃO SERVICE, deveremos, por boas práticas, colocar todas as características em uma variável.

servico = Service(ChromeDriverMenager().install())

#Sempre criamos uma variável para usar o Webdriver e o Service

navegador = webdriver.Chrome(service=servico)
#site = webdriver.Chrome(service=servico)
#paginas = webdriver.Chrome(service=servico)

from selenium.webdriver.common.by import By

navegador.get('https://www.google.com.br')

navegador.find_element(By.XPATH, '[Aqui, pesquisaremos o XPATH no site acima e iremos colar aqui para permitir que escrevemos nossa frase]').sendkeys('Digite o conteúdo que quer pesquisar.')