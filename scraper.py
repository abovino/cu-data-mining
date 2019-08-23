from requests import get
from bs4 import BeautifulSoup

res = get('https://www.westmetall.de/en/markdaten.php', stream=True).content
html = BeautifulSoup(res, 'html.parser')
del_cu_rate = html.findAll('table')[3].findAll('tr')[3].findAll('td')[1].text
eur_to_usd_ex_rate = html.findAll('table')[2].findAll('tr')[1].findAll('td')[1].text
camden_cu_rate = 3.03

print(del_cu_rate)
print(eur_to_usd_ex_rate)
print(camden_cu_rate)