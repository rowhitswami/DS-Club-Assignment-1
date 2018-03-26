#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 00:38:21 2018

@author: rowhit
"""

import pandas as pd

# Create a Pandas dataframe from the data.
df = pd.read_csv('cleaned_data.csv')

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('cleaned_excel.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Data')

# Close the Pandas Excel writer and output the Excel file.
writer.save()