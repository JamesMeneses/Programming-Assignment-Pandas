import pandas as pd
car=pd.read_csv('cars.csv')
head=car.head()
tail=car.tail()
print(car)
print(head)
print(tail)