import logging, time
import os
import sys
import requests
import trackingmoreclass
import json

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