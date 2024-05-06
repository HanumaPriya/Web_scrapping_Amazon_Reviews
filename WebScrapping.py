
# coding: utf-8

# In[16]:


from bs4 import BeautifulSoup as bs
import requests


# In[24]:


link="https://www.amazon.in/New-Apple-iPhone-Mini-128GB/product-reviews/B08L5VN68Y/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"


# In[25]:


page=requests.get(link)


# In[26]:


page


# In[27]:


page.content


# In[28]:


soup=bs(page.content,'html.parser')


# In[29]:


soup


# In[79]:


names = soup.find_all('span',class_="a-profile-name")[2:]


# In[80]:


names


# In[81]:


cust_name=[]
for i in range(len(names)):
    cust_name.append(names[i].get_text())


# In[33]:


cust_name


# In[82]:


cust_name.remove("Divyansh")


# In[35]:


cust_name


# In[83]:


cust_name.remove("Nitin Jaswant")


# In[84]:


cust_name.remove("Durga")


# In[85]:


cust_name.remove("Siddharth")


# In[86]:


cust_name


# In[87]:


len(cust_name)


# In[88]:


titles = soup.select('a.review-title span')[20:]


# In[89]:


titles


# In[90]:


len(titles)


# In[114]:


review_title = []
for i in range(len(titles)):
    review_title.append(titles[i].get_text())
review_title


# In[95]:


dates = soup.find_all('span',class_="review-date")[2:]


# In[96]:


dates


# In[97]:


len(dates)


# In[110]:


review_date = []
for i in range(len(dates)):
    review_date.append(dates[i].get_text().replace("Reviewed in India on ",""))
review_date


# In[103]:


stars = soup.select('i.review-rating span.a-icon-alt')[2:]


# In[104]:


stars


# In[105]:


len(stars)


# In[111]:


ratings = []
for i in range(len(stars)):
    ratings.append(stars[i].get_text())
ratings


# In[106]:


reviews = soup.select('span.review-text-content span')


# In[107]:


reviews


# In[108]:


len(reviews)


# In[116]:


review_content = []
for i in range(len(reviews)):
    review_content.append(reviews[i].get_text().strip("\n "))
review_content


# In[117]:


import pandas as pd


# In[118]:


df = pd.DataFrame()
df['Customer Name'] = cust_name
df['Review Title'] = review_title
df['Ratings'] = ratings
df['Date'] = review_date
df['Reviews'] = review_content


# In[119]:


df

