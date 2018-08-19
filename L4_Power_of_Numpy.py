"""Creating NumPy arrays."""

import numpy as np
import time

def get_max_index(a):
    """Return the index of the maximum value in a givrn 1D array."""
    return a.argmax()

def test_run():
    # List to 1D array
    # print(np.array([2,3,4]))
    # print (type(np.array([1,2,3])))

    # List of tuples to 2D array
    # print(np.array([(2,3,4),(5,6,7)]))

    # Empty Arrayv
    # print (np.empty((5,4,3,4)))

    # Arrays with initial values
    # print(np.ones((5,4), dtype=np.int_))
    # print(np.zeros((5,4), dtype=int))

    # Generate an array full of random numbers, uniformly sample from [0.0, 1.0]
    # print(np.random.random((5,4))) # pass in a size tuple
    # print(np.random.rand(5,4)) # function arguments (not a tuple)

    # Sample numbers from a Gaussian (normal) distribution
    # print(np.random.normal(50, 10, size=(2,3))) # "Standard normal" (mean = 0, s.d. = 1)

    # Random integers
    # print(np.random.randint(10)) # a single integer in [0, 10]
    # print(np.random.randint(0,10)) # same as above. specifying [low, high] explicit
    # print(np.random.randint(0,10, size=5)) # 5 random integers as a 1D arrays
    # print(np.random.randint(0,10, size=(2,3)))

    # Shape of array
    # a = np.random.randint(0,10,size=(5,4)) # 5x4 array of random numbers
    # print(a)
    # print(a.shape)
    # print(a.shape[0]) # number of rows
    # print(a.shape[1]) # number of columns
    # print (len(a.shape))
    # print(a.size)
    # print(a.dtype)

    # Operations on arrays
    # np.random.seed(693) # Seed the random number generator
    # a = np.random.randint(0,10, size=(5,4))
    # print("Array:\n", a)
    # print("Sum of all elements:", a.sum())

    # Iterate over rows, to compute sum of each column
    # print("Sum of each column:\n", a.sum(axis=0))

    # Iterate over columns to compute sum of each row
    # print("Sum of each row:\n", a.sum(axis=1))

    # Statistics: min, max, max, mean (across rows, cols and overall)
    # print("Minimum of each column:\n", a.min(axis=0))
    # print("Maximum of each row:\n", a.max(axis=1))
    # print("Mean of all elements", a.mean())

    # a = np.array([9,6,2,3,12,14, 7,10], dtype=np.int32)
    # print("Array:\n",a)

    # Find the maximum and its index in array
    # print("Maximum value:", a.max())

    # t1 = time.time()
    # print("Index of max:", get_max_index(a))
    # t2 = time.time()
    # print("The time taken by print statement is ", t2 - t1, " seconds")

    # a = np.random.rand(5,4)
    # print("Array:\n", a)

    # Accessing element at position(3,2)
    # element = a[3,2]
    # print(element)

    # Elements in defined range
    #print(a[0, 1:3])

    # Top left corner
    # print(a[0:2,0:2])

    # Slicing
    # Note: Slice n:m:t specifies a range that starts at n, and stops berfore m, if __name__ == '__main__':
    # print(a[:, 0:3:2])

    # Assigning a single value to an entire row
    # a[0,0] = 1
    #print("Modified array:\n", a)
    # a[0,:] = 2
    # print("Modified array:\n", a)

    # Accessing elements
    #accessing using list of indicies
    # indices = np.array([1,1,2,3])
    # print("Print value at indices:\n",a[indices])

    a = np.array([(20,25,10,23,26,32,10,5,0),(0,2,50,20,0,1,28,5,0)])
    print(a)

    # calculating Mean
    a_mean = a.mean()
    print(a_mean)

    #masking
    print(a[a<a_mean])




if __name__ == "__main__":
    test_run()
