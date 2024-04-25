# -*- coding: utf-8 -*-
"""
Creator: astaff

Sorry about the string truncating for values, it's a bit cursed but it works :P
Change it to regex if you know how to use that (I don't)
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import re
import numpy as np

date = "04.12.2024"
potential = "8V"

file_array = []
rp_array = []
fExB_array = []

#Identifiers (keep commented out)
#"rp \[m\]:"
#"fExB\(r=rp\) \[Hz\]:"

def data_finder(identifier,matchcase):
    """
    Parameters
    ----------
    identifier : The RegEx identifier for the data. Should be what precedes the data you want, 
        and any brackets/parathesis should be preceded by a forward slash
    matchcase : The variable you defined for the code anaylsis (should be f in the original code)

    Returns
    -------
    FLOAT
        Data entry following the specified identifier for the .wbg file.

    """
    start = np.subtract(re.search(identifier, matchcase).span()[1],re.search(identifier, matchcase).span()[0]) + 1
    array = re.search(identifier+".*\n", matchcase).span()
    matchcase[array[0]:array[1]]
    return float(matchcase[array[0]+start:array[1]-1])


for file in os.listdir("C:\Waterbag Solver Inputs and Outputs\Waterbag Solver Outputs\\"+date+" "+potential):
    if file.endswith(".wbs"):
        if "sol" in file:
            continue
        file_array.append(file)
        f = open("C:\Waterbag Solver Inputs and Outputs\Waterbag Solver Outputs\\"+date+" "+potential+"\\" +file, "r").read()
        rp_array.append(data_finder("rp \[m\]:",f))
        fExB_array.append(data_finder("fExB\(r=rp\) \[Hz\]:",f))
        
d = {'File Name': file_array, 'rp [m]': rp_array, 'fExB(r=rp) [Hz]': fExB_array}
df = pd.DataFrame(data=d)

plt.scatter(df['fExB(r=rp) [Hz]'],df['rp [m]'])
plt.title(date+' '+potential+'\n rp vs. fExB')
plt.xlabel('rp [m]')
plt.ylabel('fExB(r=rp) [Hz]')

df.to_csv(path_or_buf="C:\Waterbag Solver Inputs and Outputs\Waterbag Solver Outputs\\"+date+" "+potential+"\\"+date+"_"+potential+"_MCP_Data.csv",mode="w")