#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 07:34:15 2019

@author: jiyewang
"""

import csv

path  = "ingredient.csv"

#create csv file

#with open(path,'w') as f:
#    csv_write = csv.writer(f)
#    csv_head = ["ingredient","store","price","weekday"]
#    csv_write.writerow(csv_head)

#create end

stores = []

with open(path,'r',encoding='utf-8-sig') as f:
    csv_read = csv.reader(f)
    for line in csv_read:
        stores.append(line[1])

stores = stores[1:]

def check_weekday():
    global weekday
    if weekday not in weekdays:
        print("The weekday should be in 7 days of a week. Please write it again.")
        print("monday, tuesday, wednesday, thursday, friday, saturday, sunday")
        weekday = input()
        
def check_store():
    global store
    n = "n"
    if store not in stores:
        print("This store is not in the store list. Do you want to add a new store?(y/n)")
        respond = input()
        if respond == n:
            print("Please write the store again.")
            print(stores)
            store = input()
            

weekdays = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
print("Please write the name of the new ingredient.")
ingredient = input()
print("Please write where to buy it.")
store = input()
check_store()
print("How much is it?")
price = input()
print("On which weekday to buy it?")
weekday = input()
check_weekday()



with open(path,'a+',encoding='utf-8-sig',newline='') as f:
    csv_write = csv.writer(f)
    data_row = [ingredient,store,price,weekday]
    csv_write.writerow(data_row)