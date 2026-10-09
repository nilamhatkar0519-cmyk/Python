## 1D array 
import numpy as np 
arr_1D = np.array([10, 20, 30, 40, 50])

print("1D Array : ")
print(arr_1D) 


## 2D array 
arr_2D = np.array([[1, 2, 3],[4, 5, 6]])
print("\n2D Array : ")
print(arr_2D)

## 3D array 
arr_3D = np.array([[[1, 2],[3, 4]],[[5, 6],[7, 8]]])
print("\n3D Array : ")
print(arr_3D)

## operations on 2D Array 

# 1.Addition
a = np.array([[10, 20],[30, 40]])
b = np.array([5, 8]) 
print("\nAddition on 2D with 1D : ")
print(a+b)

arr1 = np.array([[10, 20],[40, 50]])
arr2 = np.array([[2, 4],[7, 9]])
print("\nAddition on 2D with 2D : ")
print(arr1 + arr2)

# 2. substraction 
print("\nSubstraction on 2D : ")
print(arr1 - arr2)

# 3. Multiplication 
print("\nMultiplication on 2D : ")
print( arr1 * arr2)

# 4. Division 
print("\nDivision on 2D : ")
print(arr1 / arr2)

# 5. Transpose 
print("\n Transpose of arr1 : ")
print(arr1.T)

print("\nTranspose of arr2 : ")
print(arr2.T)

# 6. Exponential 
print("\nExponential of arr1 : ")
print(np.exp(arr1))

print("\nExponential of arr2 : ")
print(np.exp(arr2))

## character lable 
char_arr = np.array(
    [(1, 'A'),
     (2, 'B'),
     (3, 'C')
], dtype=[('Number', 'i4'), ('Label', 'U1')])

print("\nArray with character lable : ")
print(char_arr)
print("\nLables : ")
print(char_arr['Label'])
