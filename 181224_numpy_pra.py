import numpy as np

#1
arr = np.arange(0, 4*2*4)
len(arr)
print('n1 :', len(arr))

#2
print('n2 :', arr)

#3
v=arr.reshape([4,2,4])
print('n3 :', v)

#4
print('n4 :', v.ndim)

#5
print('n5 :', v.sum())

#6
res01=v.sum(axis=0)
print('n6 :', res01)

#7
print('n7 :',res01.shape)

#8
