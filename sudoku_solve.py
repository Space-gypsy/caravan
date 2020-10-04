#!/usr/bin/env python
# coding: utf-8

# In[2]:


def check_line(vector, comm):
    if len(vector)!=9:
        print('Error: Invalid vector size')
        return None
    arr_count = [0]*len(vector)
    for i in range(len(vector)):
        if vector[i]<1 or vector[i]>9:
            print('Error: Unexceptable number at', i+1, 'point')
            return None
        arr_count[vector[i]-1] += 1
    
    if comm == 'con':
        return arr_count
    
    for i in range(len(arr_count)):
        if arr_count[i]>1:
            print('Mistake: more than one', i+1)
            return False
    return True

def check_block(block, comm):
    if len(block)!= 3 or len(block[0])!=3:
        print('Error: Invalid block shape')
        return None
    arr_count = [0]*len(block)*3
    for i in range(len(block)):
        for j in range(len(block)):
            if block[i][j]<1 or block[i][j]>9:
                print('Error: Unexceptable number at (', i+1,',', j+1, ') point')
                return None
            arr_count[block[i][j]-1] += 1
    
    if comm == 'con':
        return arr_count
    
    for i in range(len(arr_count)):
        if arr_count[i]>1:
            print('Mistake: more than one', i+1)
            return False
        
    return True


# In[9]:


vec = [1, 2, 3, 5, 5, 6, 7, 8, 9]
print(check_line(vec, 'conk'))


# In[70]:


a = [[1, 1, 1], [3, 4, 4], [5, 6, 7]]
print(check_block(a, 'conk'))


# In[11]:


# функция poly_T() считает полином Чебышёва степени degree в точке x_point
def poly_T(degree, x_point):
    T = [1, x_point, 2*x_point**2 - 1]
    if degree == 0:
        return T[0]
    
    if degree == 1:
        return T[1]
    
    count = 2
    if degree < 0:
        return None
    
    for count in range(2, degree):
        T = [T[1], T[2], 2*x_point*T[2] - T[1]]
    return T[2]


def slava_poly(degree, x):
    return ((x + (x**2 - 1)**0.5)**degree + (x - (x**2 - 1)**0.5)**degree)/2


# In[12]:


x, degree = 5, 5
print(poly_T(x, degree))
print(slava_poly(x, degree))

