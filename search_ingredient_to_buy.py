#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 09:14:35 2019

@author: jiyewang
"""

import nltk
from re import split
from nltk.corpus import stopwords
import csv

stopWords = set(stopwords.words('english'))
path  = "ingredient.csv"

ingredients = []

with open(path,"r",encoding="utf-8",errors="ignore") as r:
    c = 0
    csv_read = csv.reader(r)
    for line in csv_read:
        ingredient = line[0].strip().split(' ') 
        ingredient_name = (' ').join(ingredient)
        detail = line
        ingredients.append([ dict(ingre_name=ingredient_name.lower(), detail_doc=detail)])
        c = c+1

c = c-1
print("There are "+str(c)+" ingredients in your list.")

ingredients.remove(ingredients[0])

ingre_index = dict()

for n in range(len(ingredients)):
    tmpwords = nltk.word_tokenize(ingredients[n][0]['ingre_name'])
    for tmpword in tmpwords:
        if tmpword in ingre_index:
            ingre_index[tmpword].append(dict(index_num=n))
        else:
            ingre_index[tmpword] = [dict(index_num=n)]

print("Please enter the ingredient you want to find.")
key = input()
key = key.lower()
keys = split('\W+',key)

index_nums = []

for key in keys:
    if key in ingre_index:
        tmpresults = ingre_index[key]
        for tmpresult in tmpresults:
            tmp_num = tmpresult['index_num']
            if tmp_num not in index_nums:
                index_nums.append(tmp_num)

for num in index_nums:
    print(ingredients[num][0]['detail_doc'])
