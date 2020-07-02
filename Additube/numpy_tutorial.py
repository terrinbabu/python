import numpy as np

a = np.array([1,4,5,7])
#print(a[1])

a = np.arange(256)
#print(a)

a = np.arange(1,12,2) # a range from 1 to 12 with step of two
#print(a)

a= np.linspace(1,12,6) # linear spacing from 1 to 12 with 6 number of elements
#print(a)

a = a.reshape(3,2) # reshape the linear array to 3 rows and 2 columns
#print(a)

#print(a.size) # doesnt care the shape of the array, it gives the no. of elements
#print(a.shape) # no. of rows and columns
#print(a.dtype) # data type
#print(a.itemsize) # memory each element takes in bytes

mult_3 = a*3 # a *= 3 to save in the same array

bool_ = a<4 # check all items if its less than or equal to 4 and gives the output as a array of bools
#print(bool_)

zeros_ = np.zeros((3,4))

ones_10 = np.ones(10)

ones_ = np.ones((3,4))

x_white_px = np.array([])

b = np.array([(1.5,2,3),(4,5,6)])
print(b.ndim)

b = b.ravel() # nd array to 1d array

b = np.reshape(b, (-1, 2)) # 1d array to 2d array

#print(b)
#print(b[0])
#print(b[0][1])

a = np.array([1,4,5,7],dtype=np.int16)

np.set_printoptions(precision=2,suppress=True) # print from here on all numpy array with two decimal places and no scientific notations

sum_ = a.sum()
min_ = a.min()
max_ = a.max()
mean_ = a.mean()
var_ = a.var()
std_ = a.std()

#print(b.sum(axis=1)) # a array of sum of the each rows
#print(b.sum(axis=0)) # a array of sum of the each columns
#print(b.max(axis=1))

c = np.array([(1,2,3,4),(5,6,7,8),(9,10,11,12)])
#print(c)

#for i in c: # i = each row
    #print(i)

#for i in c.T: # i = each column
    #print(i)
    
#for i in b.flat: # i= each element
    #print(i)

#from mpl_toolkits.mplot3d import Axes3D
#import matplotlib.pyplot as plt

#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')

#x =[1,2,3,4,5,6,7,8,9,10]
#y =[5,6,2,3,13,4,1,2,4,8]
#z =[1,3,3,3,5,7,9,11,9,10]

#ax.scatter(x, y, z, marker='o')

#ax.set_xlabel('X Label')
#ax.set_ylabel('Y Label')
#ax.set_zlabel('Z Label')

#plt.show()
