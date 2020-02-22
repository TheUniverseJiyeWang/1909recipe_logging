#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 10:58:35 2019

@author: jiyewang
"""

import nltk
from re import split
from nltk.corpus import stopwords
import csv
import pandas as pd

stopWords = set(stopwords.words('english'))
stopWords.add('.')
stopWords.add(',')
path  = "recipes.csv"

recipes = []

with open(path,"r",encoding="utf-8",errors="ignore") as r:
    c = 0
    csv_read = csv.reader(r)
    for line in csv_read:
        recipe_str = " ".join(line)
        recipe = recipe_str.strip().split(' ') 
        recipe_words = (' ').join(recipe)
        detail = line
        recipes.append([ dict(recipe_doc=recipe_words.lower(), detail_doc=detail)])
        c = c+1

c = c-1
recipes = recipes[1:]
print("There are "+str(c)+" recipes in your list.")

recipe_index = dict()

for n in range(len(recipes)):
    tmpwords = nltk.word_tokenize(recipes[n][0]['recipe_doc'])
    tmpwords_index = {}
    for s in tmpwords:
        if s[-1] == '.':
            s = s.replace('.','')
        if s not in stopWords:
            if s in tmpwords_index:
                tmpwords_index[s] += 1
            else:
                tmpwords_index[s] = 1
    for s1 in tmpwords_index:
        if s1 in recipe_index:
            recipe_index[s1].append(dict(index_num=n,rank_score=tmpwords_index[s1]))
        else:
            recipe_index[s1]=[dict(index_num=n,rank_score=tmpwords_index[s1])]

print("Please enter the ingredient you have.")
key = input()
key = key.lower()
keys = split('\W+',key)

results_index = dict()
keys

for key in keys:
    if key in recipe_index:
        tmpresults = recipe_index[key]
        for i in tmpresults:
            tmpindex_num = i['index_num']
            tmprank_score = i['rank_score']
            tmpkey = tmpindex_num
            tmprecipe = recipes[int(tmpindex_num)][0]['recipe_doc']
            if tmpkey in results_index:
                tmprank_scores = results_index[tmpkey][0]['rank_scores']
                results_index[tmpkey][0]['rank_scores'] = tmprank_scores + tmprank_score + 100
            else:
                results_index[tmpkey] = [dict(recipe_all=tmprecipe,rank_scores=tmprank_score)]
                
#print(results_index)

results_df = pd.DataFrame(columns=['recipe_all','rank'])
#print(range(len(recipe_index)))

for n in range(len(results_index)):
    recipe_detail = results_index[n][0]['recipe_all']
#    print(results_index[n][0]['recipe_all'])
    rank = results_index[n][0]['rank_scores']
    results_df = results_df.append(pd.DataFrame({'recipe_all':recipe_detail,'rank':rank}, index = [n]))
#    a = {'recipe_all':recipe_detail,'rank':rank}
#    results_df.append(a,ignore_index=True)
    
results_df.sort_values(by='rank',inplace=True,ascending=False)

#print(results_df['recipe_all'][1])
for n in range(len(results_df)):
    print("The "+str(n+1)+"th recipe is:")
    print(results_df['recipe_all'][n])
