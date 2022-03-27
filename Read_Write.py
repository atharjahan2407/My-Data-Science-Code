# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 18:42:39 2022

@author: athar
"""

#-------------------------Reading & Writing data in Files----------------------

import pandas

# Reading CSV Files with Pandas:
df = pandas.read_csv('C:\Skilledge\Python\Files/User_Data.csv')
print(df)

# Writing CSV Files with Pandas:
df.to_csv('C:\Skilledge\Python\Files/IIT-B.csv')

# Reading Excel Files with Pandas
df1 = pandas.read_excel('C:\Skilledge\Python\Files/User_Data.xlsx')

df1 = pandas.read_excel('User_Data.xlsx')
print(df1)

# Writing Excel Files with Pandas 
df1.to_excel('IIT-B.xlsx')
df2 = pandas.DataFrame(df1)
print (df2)
