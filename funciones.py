import logging, time
import os
import sys
import requests
import trackingmoreclass
import json
from xml.etree import ElementTree as etree
from mydb import mydb
tracker = trackingmoreclass.track


def funcion_random_number():
  import random
  number = random.randint(0, 1000) 
  return "Numero aleatorio: {}".format(number)
  
def funcion_get_perrete():
  contents = requests.get('https://random.dog/woof.json').json()
  url = contents['url'] 
  return url

def funcion_contar_palabras(text):
  words_count = len(text.split())
  letters_count = len(''.join(text).replace(' ', ''))
  message = "Tu mensaje contiene {words} palabras y {letters} letras".format(
  words=words_count, letters=letters_count)
  return message

def funcion_track_mensajeria(text):
  urlStr = ""
  requestData = "{\"tracking_number\":\" %s \"}"%text[0]
  result = tracker.trackingmore(requestData, urlStr, "carriers/detect")
  salida = json.loads(result)
  return salida

def funcion_noticias(fuente='none'):
  
  dictUrls = {}
  bd = mydb()
  news = bd.query('SELECT * FROM tblServerRssNoticias')
  print(news)
  bd.close()



  for medio in news :
    dictUrls.update({medio[0]:medio[1]})
  

    
  if fuente == 'none': 
    submenu=[]
    disponibles=dictUrls.keys()
    for medio in disponibles:
        submenu.append('/noticias %s\n'%medio)
    return submenu

  else:
    salida = requests.get(dictUrls[fuente])
    reddit_root = etree.fromstring(salida.text)
    item = reddit_root.findall('channel/item')


    news_feed=[]
    for entry in item:   
        #get description, url, and thumbnail
        desc = entry.findtext('title') 
        link = entry.findtext('guid') 
        
        news_feed.append('%s\n%s'%(desc,link))
    return news_feed





if __name__ == '__main__':
  print(funcion_noticias('sensacine'))
# #   # bd = mydb()
# #   # salida = bd.query('SELECT * FROM tblServerRssNoticias')
# #   # bd.close()
# #   # print(salida)