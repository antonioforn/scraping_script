# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests, sys, json

data = []
def recorrerUrls(direc):
    requ = requests.get(direc)
    if requ.status_code == 200:
        html = BeautifulSoup(requ.text, 'html.parser')
        anclas = html.select("#mw-content-text li a")
        for tag in anclas:
            if tag.get('title') != None:
                print tag.get('title')
                data.append(tag.get('title'))

raiz = 'https://en.wikiquote.org'
lista = []
url = "https://en.wikiquote.org/wiki/List_of_people_by_name"


req = requests.get(url)


statusCode = req.status_code
if statusCode == 200:


    html = BeautifulSoup(req.text,'html.parser')

    anclas = html.select("center a")
    for tag in anclas:
        lista.append(raiz + tag['href'])

    i =0
    for x in lista:
        recorrerUrls(x)
        i+=1
        if i==1000:
             break
    myfile = open("filename", "w")
    #output = {"stuff": data}
    #json.dump(output, file)
    myfile.write('[')
    i =0
    for item in data:
        myfile.write('"'+ item.encode('utf8')+'",')
        #i+=1
        #if i==500: break
    myfile.write(']')
    myfile.close()

    sys.exit()




else:
    print "Status Code %d" %statusCode
