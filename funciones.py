import logging, time
import os
import sys
import requests
import trackingmoreclass
import json
from xml.etree import ElementTree as etree

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

def funcion_noticias(fuente):
  
  dictUrls = {'faro':'https://www.farodevigo.es/elementosInt/rss/1',
              'marca':'https://e00-marca.uecdn.es/rss/portada.xml',
              'el_pais':'https://elpais.com/rss/elpais/portada_completo.xml'}

  salida = requests.get(dictUrls[fuente[0]])
  #entire feed
  reddit_root = etree.fromstring(salida.text)
  item = reddit_root.findall('channel/item')
  # print (item)

  news_feed=[]
  for entry in item:   
      #get description, url, and thumbnail
      desc = entry.findtext('title') 
      link = entry.findtext('guid') 
      
      news_feed.append('%s\n%s'%(desc,link))
  return news_feed


if __name__ == '__main__':
  print (funcion_noticias(['el_pais']))