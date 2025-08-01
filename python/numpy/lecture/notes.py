import numpy as np

print(np.__version__)
print("NumPy installed successfully!")

'''NumPy is a Python library.

NumPy is used for working with arrays.

NumPy is short for "Numerical Python".

'''

'''NumPy is used to work with arrays. The array object in NumPy is called ndarray.'''



import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))


import numpy as np

arr = np.array((1, 2, 3, 4, 5))

print(arr)





'''check dimension'''

import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


'''higher'''
import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)





'''accessing element'''
import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[2] + arr[3])


'''2d'''
import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0, 1])

'''3d'''
import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])   ##6



'''slicing'''
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])##2 to 5






'''4 ke baad sab'''
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[4:])

'''4th tak'''
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[4:])


'''2 ka gap'''
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2])


import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[::2])



'''slicing 2d'''
import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4])

'''3,8'''
import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 2])