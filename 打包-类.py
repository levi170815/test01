#!/usr/bin/env python
# coding: utf-8

# In[6]:


#输入n个路径，从每个路径里选出第m帧作为m文件夹内容，
#打包每个新生成的文件夹，删除打包前的文件
import os
import shutil
def p(a0,b0,c0):
# 源文件夹路径
    a = a0
# 目标文件夹路径
    b = b0
# 遍历源文件夹中的文件
    c=os.listdir(a)
    c.sort()
    print(c)
    for i, file_name in enumerate(c,1):
        print(i,file_name)
    # 如果文件是偶数个
        if i%1 == 0:
        # 构造源文件路径和目标文件路径
            d = os.path.join(a, file_name)
            e= os.path.join(b,file_name,c0)
            if not os.path.exists(e):
                os.makedirs(e)
        # 复制文件
            shutil.copy(d,e)
p("/Users/jiajia/Desktop/c/c03","/Users/jiajia/Desktop/c/c666","qian")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




