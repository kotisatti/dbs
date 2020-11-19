# -*- coding: utf-8 -.*-
"""
Created on Wed Nov 18 19:07:48 2020

@author: Koteswararao Sathi
"""


data = [
 ("username1","phone_number1", "email1"),
 ("usernameX","phone_number1", "emailX"),
 ("usernameZ","phone_numberZ", "email1Z"),
 ("usernameY","phone_numberY", "emailX"),
 ]


identical = []
indexes =[]

for ind in range(len(data)):
    indexes.append(ind)
    for ind2 in range(ind + 1, len(data)):
        a  = set(data[ind]) & set(data[ind2])
        if a:
            identical.append([ind, ind2])
            
concat_list = [j for i in identical for j in i]
unique_list = list(set(indexes) - set(concat_list))
print([list(set(concat_list)), unique_list])            

