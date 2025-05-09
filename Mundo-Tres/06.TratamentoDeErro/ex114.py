import urllib
import urllib.error
import urllib.request
url = 'https://www.cursoemvideo.com/cursos/'

try:
    resultado = urllib.request.urlopen(url)
except urllib.error.URLerror:
    print('O site pudim não esta acessivel no momento')
else:
    print('Consegui acessar o site Pudim com sucesso')
    print(resultado.read())