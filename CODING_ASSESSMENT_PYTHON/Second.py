# Explain Pandas and numpy using Examples in PYTHON

# Pandas:-Pandas is a Python library used for working with data sets.
# Numpy: NumPy is a Python library used for working with arrays.

#       It also has functions for working in domain of linear algebra, 
#       fourier transform, and matrices.

# Examples are:
print("\nFirst Example\n")
import numpy as np 
  
# Creating array object 
arr = np.array( [[ 1, 2, 3], 
                 [ 4, 2, 5]] ) 
  
# Printing type of arr object 
print("Array is of type: ", type(arr)) 
  
# Printing array dimensions (axes) 
print("No. of dimensions: ", arr.ndim) 
  
# Printing shape of array
print("Shape of array: ", arr.shape) 
  
# Printing size (total number of elements) of array 
print("Size of array: ", arr.size) 
  
# Printing type of elements in array 
print("Array stores elements of type: ", arr.dtype) 

import numpy as np 

# Creating array from list with type float 
a = np.array([[1, 2, 4], [5, 8, 7]], dtype = 'float') 
print ("Array created using passed list:\n", a) 
  
# Creating array from tuple 
b = np.array((1 , 3, 2)) 
print ("\nArray created using passed tuple:\n", b)


# Second Example
print("\nSecond Example \n")
import csv 
  
with open('data.csv') as csvfile: 
    
    # Return a reader object which will 
    # iterate over lines in the given csvfile. 
    readCSV = csv.reader(csvfile, delimiter=',') 
    for row in readCSV: 
        print(row) 
        print(row[0]) 
        print(row[0], row[1], row[2],) 
        print("\n") 
