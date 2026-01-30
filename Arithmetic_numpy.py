#Scalar Arithmetic operations in numpy
import numpy as np
arr=np.array([1,2,3])
print(arr+5)
print(arr-2)
print(arr*2)
print(arr/2)
print(arr**2)
print(arr%2)

#vectorize math functions 
print(np.sqrt(arr))
arr1=np.array([4.4,5.7,7.5])
print(np.round(arr1))
print(np.floor(arr1))
print(np.ceil(arr1))

#Exercise
#let radius 
radius=np.array([1,2,3,4,5])
print(np.pi*radius**2)
#element wise arithmetic operations
arr2=np.array([1,2,3])
arr3=np.array([4,5,6])
print(arr2+arr3)
print(arr2*arr3)
print(arr3-arr2)
print(arr3/arr2)
print(arr3**arr2)
print(arr3%arr2)
#comparison opertions
#pass and fail in the exam
marks_arr=np.array([45,67,89,34,78])
print(marks_arr>=50)  #pass if marks >=50
print(marks_arr<50)   #fail if marks <50
print(marks_arr==50)  #exactly 50