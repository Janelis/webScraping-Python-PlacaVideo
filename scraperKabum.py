#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json
import re
from bs4 import BeautifulSoup
import time


# In[2]:


url = "https://www.kabum.com.br/hardware/placa-de-video-vga/placa-de-video-nvidia?page_number=1&page_size=100&facet_filters=&sort=most_searched"

#Informações para fingir ser um navegador
header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "accept": "application/json"
}
while(1):
    #juntamos tudo com a requests
    r = requests.get(url, headers=header)


    # In[3]:


    r.content


    # In[4]:


    soup = BeautifulSoup(r.content, 'html.parser')
    soup


    # In[5]:


    preco = soup.find_all("span",{"sc-3b515ca1-2 eqqhbT priceCard"})
    precoList = [k.text.replace(u'\xa0', u' ') for k in preco]
    precoList


    # In[6]:


    nome = soup.find_all("span",{"sc-d99ca57-0 cpPIRA sc-ff8a9791-16 dubjqF nameCard"})
    nomeList = [k.text for k in nome]


    # In[7]:


    nomeList


    # In[8]:


    dictPlacas = dict(zip(nomeList, precoList))


    # In[9]:


    dictReturn = {}
    for i in dictPlacas.keys():
        if ("2060" in i) and (("12 GB" in i) or ("12GB" in i)):
            dictReturn[i] = dictPlacas[i]

    print(dictReturn)
    k = requests.post("https://maker.ifttt.com/trigger/precokabum/with/key/KEY_WEBHOOKS_IFTTT" , data = { "value1" : str(dictReturn)})
    time.sleep(600)


# In[ ]:




