import pandas as pd
car=pd.read_csv('cars.csv')
a=car.iloc[[0,1,2,3,4],[0,2,4,6,8,10]]
b=car.iloc[[0]]
c=car.iloc[[23],[0,2]]
d=car.iloc[[1,28,18],[0,2,10]]
print(car)
print(a)
print('\n')
print(b)
print('\n')
print(c)
print('\n')
print(d)