from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

navegador = webdriver.Chrome()

#PEGA COTACAO DOLAR
navegador.get('https://www.dell.com/en-us/shop/dell-poweredge-servers/poweredge-r760-rack-server/spd/poweredge-r760/pe_r760_tm_vi_vp_sb')



valor=navegador.find_element(
    'xpath',
    '//*[@id="cf-rr-delta-response"]/div[3]/div[4]/div').get_attribute('data-price')


modelo=navegador.find_element(
    'xpath',
    '//*[@id="cf-body"]/div[4]/div[2]/div[1]/div').get_attribute('data-bv-product-id')


print(valor)


navegador.quit()

#TABELA




tabela = pd.read_excel('Produtos.xlsx')


tabela['Preço Original']  = float(valor)

tabela['Produtos']  = str(modelo)

print(tabela)

#CRIA NOVA TABELA
tabela.to_excel('ProdutoNovo.xlsx', index=False)