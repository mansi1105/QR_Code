#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install qrcode')


# In[3]:


import qrcode as qr


# In[14]:


features = qrcode.QRCode(version=1,box_size = 40,border = 5)


# In[15]:


features.add_data('https://www.youtube.come/c/GeeksforGeeks')
features.make(fit = True)


# In[16]:


generate_image = features.make_image(fill_color="blue" , back_color="white")
generate_image.save('image3.png')


# In[ ]:





# In[ ]:




