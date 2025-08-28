# Crie um código em Python que teste se o site google está acessível pelo computador usado.

import urllib.request

try:
    site = urllib.request.urlopen('http://www.google.com')
except:
    print('Ocorreu um erro ao acessar o site')
else:
    print('Site acessível')



