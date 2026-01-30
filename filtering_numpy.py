import numpy as np

#Filtering

ages=np.array([[22,33,44,55],
               [66,77,88,99]])

filter=ages[ages>50]
print(filter)
adults=ages[(ages>=18) & (ages<60)]
print(adults)
youngsters=ages[(ages<30) & (ages>0)]
print(youngsters)
evens=ages[ages%2==0]
print(evens)
odds=ages[ages%2!=0]
print(odds)
adults=np.where(ages>=33,ages,0)
print(adults)