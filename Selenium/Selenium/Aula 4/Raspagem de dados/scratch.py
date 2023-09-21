import requests
from bs4 import BeautifulSoup


link = 'https://www.google.com/search?q=cotacao+dolar'
link_two = 'https://www.ibm.com/br-pt/consulting/analytics'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.54'}
request = requests.get(link_two, headers=headers)
print(request.text)
print(request)

web = BeautifulSoup(request.text, 'html.parser')
print(web.prettify())

print('--------------------------------------------------------')
print('')
print('')

title = web.find('h1')
print(title)
print('')

paragraph = web.find('span')
print(paragraph)
print('')
print('--------------------------------------------------------')

# input = web.find_all('input')
#print(input[1])

print('')


# search_class = web.find('input', class_='SwHCTb')
# print(search_class)

print('--------------------------------------------')
print('')

depoimento_ibm = web.find('div', class_='ibm-duo-module-12a__subhead ibm-textcolor-gray-10')
print('Consultoria Data Analytics: '
      , depoimento_ibm.get_text())
print('')
print('---------------------------------------------')


