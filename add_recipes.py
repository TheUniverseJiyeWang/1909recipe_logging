#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 07:20:43 2019

@author: jiyewang
"""

import csv

path  = "recipes.csv"

#create csv file

#with open(path,'w') as f:
#    csv_write = csv.writer(f)
#    csv_head = ["name","category","recipe"]
#    csv_write.writerow(csv_head)

#create end

categories = ["vegetable","meat","carbohydrate"]

def check_category():
    global category
    if category not in categories:
        print("The category is not in the list. Please write it again.")
        print(categories)
        category = input()

print("Please write the name of the new recipe.")
name = input()
print("Please write the new recipe.")
recipe = input()
print("Which category does it belong to? (vegetable, meat or carbohydrate?)")
category = input()
check_category()

with open(path,'a+',encoding='utf-8-sig',newline='') as f:
    csv_write = csv.writer(f)
    data_row = [name,category,recipe]
    csv_write.writerow(data_row)
    


