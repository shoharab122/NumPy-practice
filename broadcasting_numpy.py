import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10])
arr1=np.array([[[11],[12],[13],[14],[15],[16],[17],[18],[19],[20]]])
result=arr+arr1
print(result)

#aggragation functions 
print(np.sum(arr))
print(np.mean(arr))
print(np.std(arr))
print(np.var(arr))
print(np.min(arr))
print(np.max(arr))
print(np.argmin(arr))
print(np.argmax(arr))
print(np.median(arr))
print(np.corrcoef(arr,arr1.flatten()))
print(np.sort(arr))
print(np.unique(arr))

#practise
array=np.array([[1,2,3,4,5,]
                ,[6,7,8,9,10]])

print(np.sum(array,axis=0)) 
print(np.sum(array,axis=1))
print(np.mean(array,axis=0))
print(np.mean(array,axis=1))