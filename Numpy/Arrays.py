import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    return numpy.flip(numpy.array(arr,float),0)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
