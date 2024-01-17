import requests
from bs4 import BeautifulSoup
import re
import pandas

#PowerEdge R760 Rack Server

url = 'https://www.dell.com/en-us/shop/dell-poweredge-servers/poweredge-r760-rack-server/spd/poweredge-r760/pe_r760_tm_vi_vp_sb'

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')



modelo = soup.find('h2', {'class': 'cf-prod-title-wrap'}).get_text()

valor = soup.find('div', {'class': 'cf-disable-tooltip'}).get_text()

#tpm = soup.find('input', n).get_text()

print('MODELO', modelo)
print('VALOR EM DOLAR DA CONFIGURACAO PADRAO DELL', valor)


