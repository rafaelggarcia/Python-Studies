import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('o site Pudim não está acessível no momento')
else:
    print('Site acessado com sucesso!')
    print(site.read()) #site.read para ler o conteúdo do site que você acabou de acessar!