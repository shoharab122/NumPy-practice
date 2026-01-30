import numpy as np
numpy_array = np.array([
    [   # Layer 0
        ['A', 'B', 'C'],   # Row 0
        ['D', 'E', 'F'],   # Row 1
        ['G', 'H', 'I']    # Row 2
    ],
    [   # Layer 1
        ['J', 'K', 'L'],
        ['M', 'N', 'O'],
        ['P', 'Q', 'R']
    ],
    [   # Layer 2
        ['S', 'T', 'U'],
        ['V', 'W', 'X'],
        ['Y', 'Z', '']
    ]
])
print(numpy_array.ndim)
print(numpy_array.shape)
print(numpy_array.size)
print(numpy_array.dtype)
print(numpy_array.itemsize)

print(numpy_array [2,1,2]) #
#construct the word "Shoharab"
word=numpy_array[2,0,0]+numpy_array[0,2,1]+numpy_array[1,1,2]+numpy_array[0,2,1]+numpy_array[0,0,0]+numpy_array[1,2,2]+numpy_array[0,0,0]+numpy_array[0,0,1]
print(word)


print(numpy_array[0:3:2])
#array[start:end:step]
print(numpy_array[0:2:1])

arr = np.array([10, 20, 30, 40, 50, 60])
print(arr[1:4:2])
print(arr[2:5:2])