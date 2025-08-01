import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  print(x)


  import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  for y in x:
    print(y)



'''x present 2d'''
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  for y in x:
    print(y)


'''The function nditer() is a helping function that can be used from very basic to very advanced iterations. It solves some basic issues which we face in iteration
, lets go through it with examples.'''
import numpy as np

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)



  import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::3]):
  print(x)
'''14 5 8'''





'''printing element with inced'''
import numpy as np

arr = np.array([[1, 2, 3],[1, 2, 3]])

for idx, x in np.ndenumerate(arr):
  print(idx, x)



'''joining two arrays'''
import numpy as np

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)


'''stack along row and coloum'''
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)

arr = np.hstack((arr1, arr2))


'''spliting'''
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 4)

print(newarr)



'''searching  using where'''
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x)




import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 0)

print(x)



'''The searchsorted() method is assumed to be used on sorted arrays.'''
import numpy as np

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)

print(x)
'''returns where 7 has to be'''


'''sorting a array'''
import numpy as np

arr = np.array([3, 2, 0, 1])

print(np.sort(arr))



'''get  A RANDOM NUMBER'''
from numpy import random

x = random.randint(100)

print(x)



