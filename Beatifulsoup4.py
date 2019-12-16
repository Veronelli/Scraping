from bs4 import BeautifulSoup

import requests

#Guardar hatml en una variable
html_doc = requests.get('https://listado.mercadolibre.com.ar/celulares#D[A:celulares,L:undefined]', headers={'Accepts-Encoding':'Indentity'})

#Guardar contenido de el html en una variable

soup = BeautifulSoup(html_doc.content, 'html.parser')

#Variable de listado de cada producto
lista = soup.find_all('span', class_='main-title')

#Oraganizar lista de productos
contenido = list()

#Variable de inicio
contador =0;

for i in lista:

    if contador <7: #Condicion para no superar la cantidad de productos

       contenido.append(i.text)#Guardar las pocisiones de los productos
       print("Producto:",i.get_text())#Imprimir Los productos segun su poccision
    
    else:
        break

    contador +=1 #Sumar le un valor al producto