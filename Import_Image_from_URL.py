#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[3]:


import os
from PIL import Image
from IPython.display import IFrame


# In[4]:


url='https://www.ibm.com/'
r=requests.get(url)


# In[5]:


r.status_code


# In[6]:


print(r.request.headers)


# In[7]:


print("request bode:", r.request.body)


# In[8]:


header=r.headers
print(header)


# In[10]:


header['date']


# In[11]:


header['Content-Type']


# In[12]:


r.encoding


# In[13]:


r.text[0:100]


# In[14]:


#You can load other types of data for non-text requests, like images. Consider the URL of the following image:

# Use single quotation marks for defining string
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'


# In[15]:


r=requests.get(url)


# In[16]:


print(r.headers)


# In[17]:


r.headers['Content-Type']


# In[18]:


path=os.path.join(os.getcwd(),'image.png')
path


# In[19]:


with open(path,'wb') as f:
    f.write(r.content)


# In[21]:


Image.open(path)


# In[ ]:





# In[ ]:




