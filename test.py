import logging, time
import os
import sys
import requests
import trackingmoreclass
import json
from xml.etree import ElementTree as etree
from mydb import mydb
tracker = trackingmoreclass.track



def funcion_get_perrete():

  headers = {'Host':'www.megadede.com',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
'Accept-Language':'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
'Accept-Encoding':'gzip, deflate, br',
'Referer':'https://www.megadede.com/series',
'X-CSRF-TOKEN':'A7Y4vSAsHHMiyj2AhYs2NGqmc1sHAlwwW2kJvfh5',
'X-Requested-With':'XMLHttpRequest',
'Connection':'keep-alive',
'Cookie':'__cfduid=d851abf22d3bc25c62c940c8f7c75bd541554053921; XSRF-TOKEN=eyJpdiI6IkhuZjlFM05VVG9aT3JUbHg1djFHTFE9PSIsInZhbHVlIjoiaHJKaFd4TEVJV1pQUklJYzkwdFZDaEpWOHdwcTJPcXY5XC9jUzNiTjFkWWU2dUc2YVFiSmd1Nm1jdlNpYnQ4Nm1sdGtUVVI2U3NLXC8xWGQ5a0Q1UkswQT09IiwibWFjIjoiY2MxMTUyYjAyYzQ3NjFiNWQ0ZDJhYzhjNThmYTBlOTE3OTBkMmE2ODU0ZGQ3OTg2ZTc5ZDI2MWM3MzdjMTc1YyJ9; cakephp_session=eyJpdiI6InBEcUVseURrYzZtcUZJbHltbVdCNGc9PSIsInZhbHVlIjoiTjFTNUVmM2pzUE4wclZnYUZhdmV3UXBhSTRMYjVzWllzaDZPU2VUMXZDZmRNUEt3Mzhsd2J1NEp5ekI0OFk4cFE1Z090azNlV2FsdXJ4bWNCY1wvUDlRPT0iLCJtYWMiOiI2NWU1MWViOGQwNmExNDAzYWIwNTFmNjcwYmNmZDcwZTQ1M2I5OWY4NGIwOGE0ZDkxYTJkZmIwNDJhZTA3ZDI1In0%3D; megadede-sess=eyJpdiI6IllZTHJNWUJHMUVUS1F2OEVVSnI5UGc9PSIsInZhbHVlIjoiY256M0tnU3QxU2laeE1wbzJsb3hHMkJvRnY2K0V1NFlRelRjbThcL0dYOVVqWTFTQ3g1MCtHUmhqUzRhM1VMSUciLCJtYWMiOiI2MDE3ZTM0ZGU2MjBiNmYwYzYxMTc5M2UyNmQ1YzA0ZGRhOWY1YWJjOTljOGFhYTFhZTFmZDE0ZjY4ZTZjMmFiIn0%3D; _ga=GA1.2.140788726.1557250830; PHPSESSID=3s6npdv7k88fog87v76b7enjk3; popshown2=1',
'TE':'Trailers'
  }
  my_cookie ={'__cfduid':'d851abf22d3bc25c62c940c8f7c75bd541554053921',
    'PHPSESSID':'3s6npdv7k88fog87v76b7enjk3',
    
        }

  contents = requests.get('https://www.megadede.com/series/all/0?quality=2&year=1990;2019',cookies=my_cookie)
  return contents






  


if __name__ == '__main__':
  salida = funcion_get_perrete()
  salida = salida.text.encode('utf-8')
  f = open("demofile2.html", "wb")
  f.write(salida)
  f.close()
  print (funcion_get_perrete())
