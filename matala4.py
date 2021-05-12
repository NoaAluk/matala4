# -*- coding: utf-8 -*-
"""
Created on Tue May 11 19:00:31 2021

@author: LENOVO
"""

import requests
import json

file = open('dests.txt','r',encoding='utf8')

d = dict()
api_key = input("Put the API key:")

#הבאת נתונים
for line in file:
    dest=line
    dest = dest.rstrip()
    try: #בדיקה האם היעד קיים
        url="https://maps.googleapis.com/maps/api/distancematrix/json?origins=תל%אביב&destinations="+dest+"&key="+api_key
        response = requests.get(url).json()  
        url2="https://maps.googleapis.com/maps/api/geocode/json?address="+dest+"&key="+api_key 
        response2 = requests.get(url2).json() 
        t=(response['rows'][0]['elements'][0]['distance']['text'],
        response['rows'][0]['elements'][0]['duration']['text'],
        response2['results'][0]['geometry']['location']['lng'],
        response2['results'][0]['geometry']['location']['lat'])
        d[dest]=t
    except:
        print('היעד',dest,'לא קיים')
        print('')
   
print('מילון יעדים:')
print(d) #הדפסת המילון
print('')

for dest in d:
    print('יעד:',dest)
    print('מרחק מתל אביב:',d[dest][0])
    print('זמן נסיעה מתל אביב:',d[dest][1])
    print('קו אורך של היעד:',d[dest][2])
    print('קו רוחב של היעד:',d[dest][3])
    print('')

#בדיקה של שלושת הערים הרחוקות ביותר מתל אביב
maxKm='0'
maxDest=''
secondMaxKm='0'
seconDest=''
thirdMaxKm='0'
thirdDest=''
for dest in d:
    km=d[dest][0]
    if km>maxKm:
        thirdMaxKm=secondMaxKm
        thirdDest=seconDest
        secondMaxKm=maxKm
        seconDest=maxDest
        maxKm=km
        maxDest=dest
        continue
    if secondMaxKm<km:
        thirdMaxKm=secondMaxKm
        thirdDest=seconDest
        secondMaxKm=km
        seconDest=dest
        continue
    if thirdMaxKm<km:
        thirdMaxKm=km
        thirdDest=dest
    
print('שלושת היעדים הרחוקים ביותר מתל אביב:')
print(maxDest,'- מרחק:', maxKm)
print(seconDest,'- מרחק:',secondMaxKm)
print(thirdDest,'- מרחק:',thirdMaxKm)



