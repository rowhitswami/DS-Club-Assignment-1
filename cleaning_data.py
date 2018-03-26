#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 01:25:08 2018

@author: rowhit
"""

# To remove future warnings
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd


df = pd.read_csv('final_data.csv', index_col='Sr.')


# Removing / from Product
df['Product'] = df['Product'].map(lambda x: x.lstrip('/'))

# Incrementing Index Value
df.index += 1
df.index.name = '#'

# Removing Special Character at the end of Product
df['Product'], df['Special_Chars'] = zip(*df['Product'].map(lambda x: x.split(' ')))
df = df.drop(df.columns[1:], axis=1) 

# Extracting Price
df['Product'], df['Price ($)'] = zip(*df['Product'].map(lambda x: x.split()))

# Extracting Date
df['Date'] = df['Product'].str.extract('(\d+)').astype(int)

# Removing Date from Product
df['Product'] = df['Product'].str.replace('\d+', '')

# Removing _ (underscore) from product
df['Product'] = df['Product'].str.replace('_', " ")

# Splitting Product column into two (Product and Salesperson)
df['Product'], df['Salesperson'] = zip(*df['Product'].map(lambda x: x.split()))

# Removing extra characters from Product, Salesperson and Price ($)
df['Product'] = df['Product'].map(lambda x: x.lstrip('PR:'))
df['Salesperson'] = df['Salesperson'].map(lambda x: x.lstrip('SP:'))
df['Price ($)'] = df['Price ($)'].map(lambda x: x.lstrip('$'))

# Formatting Date
df["Date"] = pd.to_datetime(df["Date"], format='%Y%m%d', errors='ignore')

# Saving Cleaned Data in a CSV file
#df.to_csv('cleaned_data.csv')
print(df)