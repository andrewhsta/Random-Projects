# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 16:10:23 2024

@author: astaff
"""

import pandas as pd
import matplotlib.pyplot as plt
date = "04.12.2024"
potential = "8V"

df = pd.read_csv("C:\Waterbag Solver Inputs and Outputs\Waterbag Solver Outputs\\"+date+" "+potential+"\\"+date+"_"+potential+"_MCP_Data_new.csv",index_col=0)

plt.figure()
plt.scatter(df['fExB(r=rp) [Hz]'],df['rp [m]'])
plt.title(date+' '+potential+'\n rp vs. fExB')
plt.xlabel('rp [m]')
plt.ylabel('fExB(r=rp) [Hz]')
#plt.savefig("C:\Waterbag Solver Inputs and Outputs\Waterbag Solver Outputs\\11.24.2023 "+potential+"\\"+date+"_"+potential+"_rotwafreqvsrp.pdf")

plt.figure()
plt.scatter(df['Rotating Wall Frequency [kHz]'],df['rp [m]'])
plt.title(date+' '+potential+'\n Rotating Wall Frequency vs. rp')
plt.xlabel('Rotating Wall Frequency [kHz]')
plt.ylabel('rp [m]')
#plt.savefig("C:\Waterbag Solver Inputs and Outputs\Waterbag Solver Outputs\\"+date+" "+potential+"\\"+date+"_"+potential+"_rotwafreqvsrp.pdf")

plt.figure()
plt.scatter(df['Rotating Wall Frequency [kHz]'], df['fExB(r=rp) [Hz]'])
plt.title(date+' '+potential+'\n Rotating Wall Frequency vs. fExB')
plt.xlabel('Rotating Wall Frequency [kHz]')
plt.ylabel('fExB(r=rp) [Hz]')
#plt.savefig("C:\Waterbag Solver Inputs and Outputs\Waterbag Solver Outputs\\"+date+" "+potential+"\\"+date+"_"+potential+"_rotwafreqvsfexb.png")