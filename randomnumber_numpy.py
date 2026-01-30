import numpy as np

rng = np.random.default_rng(seed=(22))
print(rng.integers(low=1, high=60,size=(3,2)))

print(np.random.uniform(low=-1, high=1, size=(2,3)))

#suffle array
rng= np.random.default_rng()
arr = np.array([1,2,3,4,5,6,7,8,9,10])
rng.shuffle(arr)
print(arr)

arr1=np.array(['apple','banana','cherry','mango'])
arr1=rng.choice(arr1,size=3)
print(arr1)