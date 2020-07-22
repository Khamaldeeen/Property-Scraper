import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

df = pd.read_csv("3 Bedroom Apart.csv", sep=',')


def Park(x):
    if "Parking" in x:
        y = x.split()
        return int(y[-3])
    else:
        return 0

df['Parking Spaces'] = df['Extra Features'].apply(Park)

def Toilet(x):
    y = x.split()
    if "Toilets" in y and len(y) < 4:
        return int(y[2])
    elif "Toilets" in y and len(y) > 4:
        return int(y[4])
    else:
        return 0

df['Toilets'] = df['Extra Features'].apply(Toilet)

def baths(x):
    if "Bathrooms" in x:
        y = x.split()
        return int(y[2])
    else:
        return 0

df['Baths'] = df['Extra Features'].apply(baths)
lis = ['Location', 'Parking Spaces', 'Toilets', 'Baths', 'Price']
df = df[lis]

df.to_csv('Wrangled 3 Bedroom.csv', index=False)
