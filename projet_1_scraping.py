# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 15:08:02 2022

@author: arnau
"""

# Importation des librairies
from bs4 import BeautifulSoup
import requests
import csv

    
lien = "http://books.toscrape.com/" #Introduce the web address

response = requests.get(lien)

soup = BeautifulSoup(response.text, "html.parser")

soup = soup.find(class_="nav nav-list")

liste_liens            =  []
liste_genres           =  []
for link in soup.find_all('a'):
    link = link.get('href')
    if len(link) > 22 and 'books_1' not in link :
        liste_liens.append(link)
        link = (link.split("/", 3)[3]).split("_", 1)[0]
        liste_genres.append(str(link).capitalize())
    
for genre in liste_genres :
    
    # Définition des variables

    pages_url              =  []
    title                  =  []
    lien_page_livre        =  []
    product_page_url       =  []
    universal_product_code =  []
    price_including_tax    =  []
    price_excluding_tax    =  []
    number_available       =  []
    product_description    =  []
    category               =  []
    review_rating          =  []
    image_url              =  []
    donnees                =  []
    
    header                 =  [
              'product_page_url',
              'universal_product_code',
              'title',
              'price_including_tax',
              'price_excluding_tax',
              'number_available',
              'product_description',
              'category',
              'review_rating',
              'image_url'
                              ]
    
    data                   =  []

    lien = "http://books.toscrape.com/"+liste_liens[liste_genres.index(genre)]
    response = requests.get(lien)
    soup = BeautifulSoup(response.text, "html.parser")
    
    pages_url.append(lien)
    
    # le nombre de page
    soup_2      = soup.find(class_="form-horizontal")
    pages       = int(int((str(soup_2).split(">", 4)[4]).split("<", 1)[0])/20)+1
    
    if pages > 1 :
        for i in range(2,pages+1):
            lien_2 = lien.replace('index.html','page-'+str(i)+'.html')
            pages_url.append(lien_2)
            
        # on récupère les titres

    for i in pages_url :
        response = requests.get(i)
        soup = BeautifulSoup(response.text, "html.parser")
       
        for link in soup.find_all('article'):
            title.append((str(link.find('h3')).split('title=', 1)[1]).split('">', 1)[0])

        # on récupère l'url du livre
            addresse_livre = 'http://books.toscrape.com/catalogue/'+ str(link.find('h3')).split('/',3)[3].split('"',1)[0]
            product_page_url.append(addresse_livre)
            
    
        # on récupère le code, les prix, les stocks, la description
            lien = addresse_livre
            response = requests.get(lien)
            soup = BeautifulSoup(response.text, "html.parser")
            
            universal_product_code.append(soup.find_all('td')[0].string)
            
            price_excluding_tax.append(str(soup.find_all('td')[2].string).replace('Â£',''))
            
            price_including_tax.append(str(soup.find_all('td')[3].string).replace('Â£',''))
            
            number_available.append((str(soup.find_all('td')[5].string).split('(',1)[1]).replace(' available)',''))
            
            try :
                product_description.append(((str(soup.find_all(class_='product_page')).split('<p>',1)[1]).split('</p>',1)[0]).replace('â',"'"))
            except: 
                product_description.append('')
            
            category.append(str(soup.find_all('td')[1].string))
            
            review_rating.append((str(soup.find_all(class_='star-rating')).split('rating ',1)[1]).split('">',1)[0])
            
            image_url.append("https://books.toscrape.com/" + (str(soup.find_all(class_='item active')).split('../',2)[2]).split('"/',1)[0])
        
    

    for j in range(len(image_url)):
        sub_data = [
                product_page_url[j],
              universal_product_code[j],
              title[j],
              price_including_tax[j],
              price_excluding_tax[j],
              number_available[j],
              product_description[j],
              category[j],
              review_rating[j],
              image_url[j]
              ]
        data.append(sub_data)
        
    with open( genre +'.csv', 'w+', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)          
            


