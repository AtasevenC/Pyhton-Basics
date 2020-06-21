#!/usr/bin/env python
# coding: utf-8

# # Create the NumPy Array

# In[53]:


import numpy as np 


# In[54]:


np.array ([1,2,3,4,5])


# In[55]:


a= np.array([1,2,3,4,5])


# In[56]:


type(a)


# ## Let create an array 

# In[57]:


np.zeros(10,dtype=int)


# In[58]:


np.ones(10, dtype =int)


# In[59]:


np.ones((3,5))


# In[60]:


np.full((3,5),7)


# In[61]:


np.arange(0,31,3)  # Here we strat to go from 0 to 31 and we increase the series 3


# In[62]:


np.linspace(0,2,5) # we divide 5 parts


# In[63]:


np.linspace(0,1,100)


# In[64]:


np.random.normal(10,4,5) # here aritmatic ort= 10 stdandrtSp=4 and 5 number


# In[65]:


np.random.normal(10,4,3)


# In[66]:


np.random.normal(1,0,3)


# In[67]:


np.random.normal(5,4,(3,4))  


# In[68]:


np.random.randint(0,10,3) # random int between 0 and 10, 3 numbers


# In[69]:


np.random.randint(0,20,(3,3))


# * np.arange 
# * np.random.normal
# * np.linespace
# * np.random.randint

#   up the here we studied some fonction of **NumPy array** and some ?_properties_

# In[70]:


np.random.randint(10, size=10)


# In[71]:


a=np.random.randint(10, size=10)


# In[72]:


a.ndim  # dimension number


# In[73]:


a.shape


# In[74]:


a.size


# In[75]:


a.dtype


# In[76]:


b= np.random.randint(10, size=(3,5))


# In[77]:


b


# In[78]:


b.ndim


# In[79]:


b.shape


# In[80]:


b.size


# In[81]:


b.dtype


# # Reshaping

# In[82]:


np.arange(1,10)


# In[105]:


a=np.arange(1,10)


# In[106]:


a.reshape((3,3))


# # Concatenation

# In[107]:


x= np.array([1,2,3])
y= np.array([4,5,6])


# In[109]:


np.concatenate([x,y])


# In[112]:


z=np.array([7,8,9])


# In[115]:


np.concatenate([x,y,z])


# In[116]:


a=np.array([[1,2,3],[4,5,6]])


# In[117]:


a


# In[118]:


np.concatenate([a,a],axis=1)


# # Spliting

# In[120]:


x= np.array([1,2,3,99,99,3,2,1])


# In[121]:


np.split(x,[3])


# In[123]:


np.split(x,[3,5])


# In[124]:


a,b,c=np.split(x,[3,5])


# In[125]:


a


# In[126]:


b


# In[127]:


c


# In[129]:


m= np.arange(16).reshape(4,4)
m


# In[130]:


np.vsplit(m,[2])


# In[131]:


np.vsplit(m,[1])


# In[132]:


np.vsplit(m,[1,2,3])


# In[133]:


a,b,c,d=np.vsplit(m,[1,2,3])


# In[134]:


a


# In[135]:


b


# In[136]:


c


# In[137]:


d


# In[138]:


m


# In[139]:


np.hsplit(m,[1,2,3])


# In[140]:


x,y,z,t=np.hsplit(m,[1,2,3])


# In[141]:


x


# In[142]:


y


# In[143]:


z


# In[144]:


t


# # Sorting

# In[145]:


v=np.array([4,25,7,9,8,1])


# In[146]:


v


# In[147]:


np.sort(v)


# In[148]:


v


# In[149]:


v.sort()


# In[150]:


v


# In[152]:


type(v)


# In[153]:


m=np.random.normal(20,5,(3,3))


# In[154]:


m


# In[155]:


np.sort(m,axis=1)


# In[156]:


np.sort(m,axis=0)


# In[158]:


np.sort(m)


# In[160]:


m= np.random.randint(10,size=(3,5))


# In[161]:


m


# In[162]:


m[1,3]


# In[163]:


m[0,1]


# In[164]:


m[0,1]=100


# In[165]:


m


# # Slicing 

# In[166]:


a= np.arange(20,30)


# In[167]:


a


# In[168]:


a[0:3]


# In[169]:


a[3:]


# In[170]:


a[1::2]


# In[171]:


m= np.random.randint(10,size=(5,5))


# In[172]:


m


# In[173]:


m[:,0]


# In[174]:


m[4,:]


# In[175]:


m[0:2,0:3]


# In[ ]:




