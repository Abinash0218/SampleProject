import numpy as np

arr=np.array([1,2,3,4,5])
print(arr)
print(arr.size)
print(arr[4])
print(arr[0])
print(np.sum(arr))
print(np.mean(arr))
print(np.min(arr))
print(np.max(arr))

print(arr+2)
print(arr-2)
print(arr*2)
print(arr**2)
print(arr/2)
print(arr%2)

a=np.zeros(4)
b=np.ones(4)
c=np.arange(0,9)
print(a)
print(b)
print(c)

arr1=np.array([[1,2],[3,4],[5,6]])
print(arr1)
print(arr1[1][0])
print(arr1[2][1])
print(arr1.shape)
print(arr1.size)

arr2=np.arange(9)
print(arr2)
print(arr2.reshape(3,3))

# random module
print(np.random.rand(3))
print(np.random.randint(1,10,5)) # 5->to tell the no.of random numbers between 1-9

# linear algebra module
arr3=np.array([[1,2],[3,4]])
print(round(np.linalg.det(arr3))) # to find the determinant of the 2D array like ((1*4)-(2*3))=4-6=-2
print(np.linalg.inv(arr3)) # this is the concept of multipling A*(A)-1=I

arr4=np.array([3,4,9])
print(np.sqrt(arr4))
print(np.exp(arr4))
print(np.log(arr4))

arr5=np.array([9,5,10,3,2])
print(np.sort(arr5))
print(np.argsort(arr5))
result=np.where(arr5>3)
print(result) # shows the index of the array where the condition is true
arr6=np.concatenate((arr4,arr5))
print(arr6)
print(np.split(arr6,2)) # divides the array into two equal parts
print(np.unique(arr6)) # prints the unique elements in a sorted way

d=np.array([1,2,3])
e=np.array([4,5,6])
f=np.array([7,8,9])
print(np.stack((d,e,f))) # combines two or more 1D array with the same size to a 2D array

print(np.clip(arr6,5,10)) # convert the values less than 5 to 5 in the array and convert the values greater than 10 to 10 and the values btw thw range of 5-10 remains same in the array
  