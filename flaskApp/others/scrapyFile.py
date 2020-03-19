import urllib.request
from geopy.geocoders import Nominatim
from bs4 import BeautifulSoup
from python_countries import CountriesApi
from googletrans import Translator

URL='https://www.worldometers.info/coronavirus/'
soup = BeautifulSoup(urllib.request.urlopen(URL))
client=CountriesApi()

def prevediVest(vest):
    translator=Translator()
    return translator.translate(vest,dest='hr').text
    

def vratiKoordinate(drzava):
        try:
            geolocator = Nominatim(user_agent="my_app")
            location = geolocator.geocode(drzava)
            return [location.latitude,location.longitude]
        except:
            return [0,0]



def redoviTabele():
    tabela=soup.find('table',{'id':'main_table_countries_today'})
    redoviPOlje=tabela.find_all('tbody')[0]
    redovi=[]
    drzave=[]
    for i in redoviPOlje.find_all('tr'):
        dir={}
        lista=[]
        for index,j in enumerate(i.find_all('td'),start=0):
            bezSpace=j.text.strip(' ')
            bezZareza=bezSpace.replace(',','')
            bezPlus=bezZareza.strip('+')
            if bezPlus=='':
                bezPlus=0
            try:
                lista.append(float(bezPlus))    
            except:
                lista.append(bezPlus)
        drzave.append(lista[0])
        redovi.append(lista)
    return redovi

def vestiNaslovi(start,end):
    vesti=soup.find_all('li',{'class':'news_li'})
    lista=[]
    for i in vesti[start:end]:
        dir={}
        vrednost=i.text.replace('[source]','')
        vrednost=vrednost.replace('\n','')
        vrednost=vrednost.replace(u'\xa0','')
        reci=vrednost.split(' ')
        if(len(reci)>20):
            reci[20:]=''
            vrednost=' '.join([str(elem) for elem in reci])
            vrednost=vrednost.replace(vrednost[80:],'')
            vrednost+='...'
        dir['naslov']=vrednost
        try:
            dir['url']=i.find_all('a',{'class':'news_source_a'})[0].get('href')   
        except:
            dir['url']=None
        lista.append(dir)
    return lista

def domaceVesti():
    vesti=soup.find_all('li',{'class':'news_li'})
    domace=[]
    for i in vesti:
        if 'Serbia' in i.text or 'Serbian' in i.text:
            dir={}
            dir['naslov']=prevediVest(i.text.replace('[source]',''))
            try:
                dir['url']=i.find_all('a',{'class':'news_source_a'})[0].get('href')
            except:
                dir['url']=None
            domace.append(dir)
    return domace

def stanjeSrbija():
    url='http://www.blic.rs/vesti/drustvo/korona-virus-najnovije-vesti/p388f8p'
    strana=BeautifulSoup(urllib.request.urlopen(url))
    informacije=strana.find('div',{'class':'article-body'})
    info=[]
    for i in informacije.find_all('ul')[0].find_all('li'):
        info.append(i.text)
    return info


for i in stanjeSrbija():
    print(i)
