#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np

def check_string(s1,s2):
    arr1 =np.array(list(s1))
    arr2 =np.array(list(s2))

    common_char=np.isin(arr1, arr2)
    common_str = ''.join(arr1[common_char])

    uncommon_char_s1 =np.setdiff1d(arr1, arr2)
    uncommon_char_s2 =np.setdiff1d(arr2, arr1)

    uncommon_str_s1 =''.join(uncommon_char_s1)
    uncommon_str_s2 =''.join(uncommon_char_s2)
    
    if common_str:
        print("Yes")
        print(f"String1: {common_str}")
        print(f"String2: {uncommon_str_s1},{uncommon_str_s2}")
    else:
        print("No")

s1 = "Refer"
s2 = "Regfree"
check_string(s1, s2)


# In[6]:


import numpy as np

def reverse_words(s):

    words = np.array(s.split())
    
   
    reversed_words = [''.join(np.flip(list(words))) for words in words]
    
   
    reversed_string = ' '.join(reversed_words)
    
    print(reversed_string)

input_string = "ViDeo SurVeiLLance SyStems"
reverse_words(input_string)


# In[ ]:




