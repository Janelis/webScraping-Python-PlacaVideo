#!/usr/bin/env python
# coding: utf-8

#Bibliotecas
import requests
import re
from bs4 import BeautifulSoup
import time

#URL onde buscarei os dados
url = "https://www.kabum.com.br/hardware/placa-de-video-vga/placa-de-video-nvidia?page_number=1&page_size=100&facet_filters=&sort=most_searched"

#Header para atuar como navegador para o site
header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "accept": "application/json"
}

#Request do site
r = requests.get(url, headers=header)
    
#Processamento do get pelo BeautifulSoup
soup = BeautifulSoup(r.content, 'html.parser')
    
#Obtencao dos dados de preco
preco = soup.find_all("span",{"sc-3b515ca1-2 eqqhbT priceCard"})
precoList = [k.text.replace(u'\xa0', u' ') for k in preco]
    
#Obtencao dos dados de nome
nome = soup.find_all("span",{"sc-d99ca57-0 cpPIRA sc-ff8a9791-16 dubjqF nameCard"})
nomeList = [k.text for k in nome]

#Dicionario com nomes e precos **CONSIDERA QUE OS PRECOS E NOMES VEM NA MESMA ORDEM**
dictPlacas = dict(zip(nomeList, precoList))

#Filtragem dos dados para a placa RTX 2060 - 12GB
dictReturn = {}
for i in dictPlacas.keys():
    if ("2060" in i) and (("12 GB" in i) or ("12GB" in i)):
        dictReturn[i] = dictPlacas[i]

print(dictReturn)
    
#Request que envia os dados para um WebHook do site IFTTT, que já administra a posterior passagem para um bot no Discord. 
#Chave escondida.
k = requests.post("https://maker.ifttt.com/trigger/precokabum/with/key/KEY_WEBHOOKS_IFTTT" , data = { "value1" : str(dictReturn)})
    
    
    
    
