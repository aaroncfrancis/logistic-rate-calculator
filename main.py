import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# df1 = pd.read_csv('data_origin_mtl.csv')

#defining function, filter and adding column with a calculation 
def f(origin, destination, weight):
    df1 = pd.read_csv('data_origin_mtl.csv')
    filtered = df1[(df1['Origin']==origin) & (df1['Destination']==destination)]
    filtered['Rate'] = filtered['Rate / 100 lbs'] * (1/100) * weight
    return filtered

answer = 'n'

while answer == 'n': 
    origin = input('What is your origin? (ex: "Montreal") ')
    destination = input('What is your destination? (ex: "Toronto")')
    weight = input('What is the weight of your shipment? ')
    weight = float(weight)
    # print(origin, destination, weight)
    answer = input('Is this information correct? Yy/Nn ?')
    answer = answer.lower()
    filteredf = f(origin, destination, weight)
    print(filteredf)
    # filteredf.info() # prints out the names of the coloumns

carriers = list(filteredf['Carrier'])
rates = list(filteredf['Rate'])

plt.bar(carriers,rates)
plt.show()

wtype = ['cw','aw']
for type in wtype:
    if type == 'cw':
        length = float(input('What is the length (in inches) of your load?'))
        width = float(input('What is the width (in inches) of your load?'))
        depth = float(input('What is the depth (in inches) of your load?'))
    elif type == 'aw':
        actual_weight = (input('What is the weight in lbs of your load?'))