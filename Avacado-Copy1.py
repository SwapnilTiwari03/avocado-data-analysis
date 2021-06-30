#!/usr/bin/env python
# coding: utf-8

# ---
# # **Table of Contents**
# ---
# 
# 1. [**Introduction**](#Section1)<br>
# 2. [**Problem Statement**](#Section2)<br>
# 3. [**Installing & Importing Libraries**](#Section3)<br>
#   3.1 [**Installing Libraries**](#Section31)<br>
#   3.2 [**Upgrading Libraries**](#Section32)<br>
#   3.3 [**Importing Libraries**](#Section33)<br>
# 4. [**Data Acquisition & Description**](#Section4)<br>
# 5. [**Data Pre-Profiling**](#Section5)<br>
# 6. [**Data Pre-Processing**](#Section6)<br>
# 7. [**Data Post-Profiling**](#Section7)<br>
# 8. [**Exploratory Data Analysis**](#Section8)<br>
# 9. [**Summarization**](#Section9)</br>
#   9.1 [**Conclusion**](#Section91)</br>
#   9.2 [**Actionable Insights**](#Section91)</br>
# 
# ---

# # 1. Introduction
# ______________________________________________________________________________________________________
#  
# It is a well known fact that Millenials LOVE Avocado Toast. It's also a well known fact that all Millenials live in their parents basements.Clearly, they are not buying home because they are buying too much Avocado Toast! They spend nearly dollar 900,000 per month on it, according to data from payment company Square, as reported by Time. Avocado toast sales are also rising quickly. In June 2014, Americans were only buying dollar 17,000 worth of the breakfast per month, compared to dollar 890,500 in June 2017.But maybe there's hope… if a Millenial could find a city with cheap avocados, they could live out the Millenial American Dream.
# - Please refer site https://www.cnbc.com/2017/07/21/americans-spend-900000-a-month-on-avocado-toast.html#:~:text=Gurner%20exaggerated%20the%20price%20consumers,that's%20certainly%20not%20the%20rule
# 

# # Probem Statement
# _____________________________________________________________________________________________________________
# 
#  * Q.1 Which type of Avocados are more in demand (Conventional or Organic)?
#  * Q.2 In which range Average price lies, what is distribution look like?
#  * Q.3 How Average price is distributed over the months for Conventional and Organic Types?
#  * Q.4 What are TOP 5 regions where Average price are very high?
#  * Q.5 What are TOP 5 regions where Average consumption is very high?
#  * Q.6 In which year and for which region was the Average price the highest?
#  * Q.7 How price is distributed over the date column?
#  * Q.8 How dataset features are correlated with each other?
# 
# ![513T70+8siL._SX466_.jpg](attachment:513T70+8siL._SX466_.jpg)

# ---
# <a id = Section3></a>
# # **3. Installing & Importing Libraries**
# ---
# 
# - This section is emphasised on installing and importing the necessary libraries that will be required.

# ### **Installing Libraries**

# In[1]:


get_ipython().system('pip install --user numpy                                    ')
get_ipython().system('pip install --user pandas')
get_ipython().system('pip install --user matplotlib pandas seaborn bokeh plotly')
get_ipython().system('pip install --user pandas-profiling')


# ### **Upgrading Libraries**
# 
# - **After upgrading** the libraries, you need to **restart the runtime** to make the libraries in sync.
# 
# - Make sure not to execute the cell under Installing Libraries and Upgrading Libraries again after restarting the runtime.

# In[2]:


#!pip install pandas-profiling -U  
#sudo pip3 install pandas-profiling --upgrade  # Upgrading pandas profiling to the latest version


# ### **Importing Libraries**
# 
# - You can headstart with the basic libraries as imported inside the cell below.
# 
# - If you want to import some additional libraries, feel free to do so.
# 

# In[3]:


import numpy as np
np.set_printoptions(precision=4)

import pandas as pd
pd.set_option('mode.chained_assignment', None)      # To suppress pandas warnings.
pd.set_option('display.max_colwidth', -1)           # To display all the data in each column
pd.options.display.max_columns = 50                 # To display every column of the dataset in head()

import matplotlib.pyplot as plt                                     # Importing pyplot interface to use matplotlib
plt.style.use('seaborn-whitegrid')                  # To apply seaborn whitegrid style to the plots.
get_ipython().run_line_magic('matplotlib', 'inline')

import seaborn as sns
sns.set(style='whitegrid', font_scale=1.3, color_codes=True)      # To adjust seaborn settings for the plots.

import pandas_profiling

import warnings
warnings.filterwarnings("ignore")
warnings.filterwarnings("ignore",category=DeprecationWarning)

            


# # Data Acquistion & Description
# __________________________________________________________________________________________________________________________
# * This data was downloaded and provided by INSAID, from the Hass Avocado Board website in May of 2018 & compiled into a single CSV.
# * Represents weekly 2018 retail scan data for National retail volume (units) and price.
# * The dataset comprises of 18249 observations of 14 columns. Below is a table showing names of all the columns and their description.
# * The unclear numerical variables terminology is explained in the next section:
# 
# |Id|Feature|Description|
# |:--|:--|:--|
# |01| Unnamed:0              | Its just a useless index feature that will be removed later.|
# |02| Total Volume           | Total sales volume of avocados.|
# |03| 4046                   | Total sales volume of Small/Medium Hass Avocado.|
# |04| 4225                   | Total sales volume of Large Hass Avocado.| 
# |05| 4770                   | Total sales volume of Extra Large Hass Avocado.|
# |06| Total Bags             | Total number of Bags sold.| 
# |07| Small Bags             | Total number of Small Bags sold.|
# |08| Large Bags             | Total number of Large Bags sold.|
# |09| XLarge Bags            | Total number of XLarge Bags sold.|
# 
# 

# ### *Let's understand the data:*
#  - This data has 18249 rows and 14 columns

# In[4]:


data = pd.read_csv("https://raw.githubusercontent.com/insaid2018/Term-2/master/Projects/avocado.csv")
print('Data Shape:', data.shape)
data.head()


# In[5]:


data.columns # It will give all the column names of data set


# In[6]:


data.head() # It will give the first 5 records of data set


# In[7]:


data.tail() # It wil give you last 5 records of data set


# ### **Data Description**
# 
# - To get some quick description out of the data I am using describe  method defined in pandas library.

# In[8]:


data.describe()


# ### **Data Information**
# - This data set has no null values. Looks line it does not contain any missing values
# - Average Price is having almost a normal distribution as mean(1.405978) value is close to medain (1.370000) value
# - the distribution of Large Bags is positive (right) skewed because the mean of Large Bags (5.433809e+04) lies to the right of the median (50%) value(2.636282e+04) , on a distribution plot.
# - Similarly comparing the 75% and max values of the XLarge Bags columns we can see that there are outliers present in some other columns.

# In[9]:


data.info()


# In[10]:


data.isnull().sum() # Will show null count for each column


# ---
# <a name = Section5></a>
# # **5. Data Pre-Profiling**
# ---
# 
# - This section is emphasised on getting a report about the data.
# 
# - You need to perform pandas profiling and get some observations out of it...

# In[11]:


profile = data.profile_report(title="Avacado's Profiling before Data Preprocessing", progress_bar=False, minimal=True)
profile.to_file(output_file="Avacado's_profiling_before_preprocessing.html")


# - I have done Pandas Profiling before preprocessing dataset, so we can get initial observations from the dataset in better visual aspects, to find correlation matrix and sample data. File was saved as html file Avocado_before_preprocessing.html.
# 
# - Will take a look at the file and see what useful insight you can develop from it.
# 
# - Initial observation as a result from profiling of Avocado Dataset can be seen in Avocado_before_preprocessing.html
# 
# ![image.png](attachment:image.png)
# ![image.png](attachment:image.png)
# 

# ---
# <a name = Section6></a>
# # **6. Data Pre-Processing**
# ---
# 
# - This section is emphasised on performing data manipulation over unstructured data for further processing and analysis.
# 
# - To modify unstructured data to strucuted data you need to verify and manipulate the integrity of the data by:
#   - Handling missing data,
# 
#   - Handling redundant data,
# 
#   - Handling inconsistent data,
# 
#   - Handling outliers,
# 
#   - Handling typos

# - The Feature "Unnamed:0" is just a representation of the indexes, so it's useless to keep it, lets remove it now !

# In[12]:


data.drop('Unnamed: 0',axis=1,inplace=True)


# - Let's check the data head again to make sure the feature Unnamed:0 is removed.

# In[13]:


data.head()


# - Earlier info we have seen date is an object datatype not the date data type. So Let's change it's type to the date type.

# In[14]:


data['Date']=pd.to_datetime(data['Date'])
data['Month']=data['Date'].apply(lambda x:x.month)
data['Day']=data['Date'].apply(lambda x:x.day)


# In[15]:


data.head()


# ---
# <a name = Section7></a>
# # **7. Data Post-Profiling**
# ---
# 
# - This section is emphasised on getting a report about the data after the data manipulation.
# - You may end up observing some new changes, so keep it under check and make right observations.
# 

# In[16]:


profile = data.profile_report(title="Avacado's Profiling after Data Preprocessing", progress_bar=False, minimal=True)
profile.to_file(output_file="Avacado's_profiling_after_preprocessing.html")


# - As we can see now there are 11 numerical , 3 categorical and 1 date columns .
# 
# ![image.png](attachment:image.png)
# ![image.png](attachment:image.png)

# ---
# <a name = Section8></a>
# # **8. Exploratory Data Analysis and Question answered**
# ---
# 
# - Organic vs Conventional : The main difference between organic and conventional food products are the chemicals involved during production and processing. The interest in organic food products has been rising steadily over the recent years with new health super fruits emerging. Let's see if this is also the case with our dataset
# 

# ### Q.1 Which type of Avocados are more in demand (Conventional or Organic)?

# In[34]:


Type=data.groupby('type')['Total Volume'].agg('sum')
print(Type)
labels = 'conventional','organic'
sizes = [Type['conventional'], Type['organic']]
colors = ['yellowgreen', 'lightcoral']
#explode = (0.1, 0, 0, 0)  # explode 1st slice

# Plot
plt.pie(sizes, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.title('Pie chart showing the proportion of each Type of avacado in demand')
plt.show()
        


# - Just over 2% of our dataset is organic. So looks like Conventional is in more demand. Now, let's look at the average price distribution

# ### Q2. In which range Average price lies, what is distribution look like?

# In[35]:


data['AveragePrice'].plot(kind='kde', figsize=(15, 7), color='black')
plt.xlabel('Average Price')
plt.ylabel('Density')
plt.title('KDE plot showing the density of Average price values')


# ### Q3. How Average price is distributed over the months for Conventional and Organic Types

# In[36]:


#df.groupby('type')['Total Volume'].agg('sum')
plt.figure(figsize=(18,10))
sns.lineplot(x="Month", y="AveragePrice", hue='type', data=data)
plt.title('Average price distrbution over month for conventional and organic types')
plt.show()


# - Looks like there is spike in sales in month of 8-10 for both Conventional and Organic types of avacado prices

# ### Q.4 What are TOP 5 regions where Average price are very high?

# In[37]:


(data.groupby('region')['AveragePrice'].agg('sum')/len(data)).plot.bar(figsize=(24,10), colormap='Dark2', fontsize=13,)
plt.xlabel('region')
plt.ylabel('Averge Price')
plt.title('Bar Chart showing the Average price in different region')


# #### Looks like these regions are where price is very high
#  * HartfordSpringfield
#  * SanFrancisco
#  * NewYork
#  * Philadelphia
#  * Sacramento

# ### Q.5 What are TOP 5 regions where Average consumption is very high?
# - First need to remove filter data ans I dont want to show the average consumption at Us level , so removing rows having region name TotalUS
# - 

# In[38]:


subsetdata=data[data['region']!='TotalUS']
#(data.groupby('region')['AveragePrice'].agg('sum')/len(data)).plot.bar(figsize=(24,10), colormap='Dark2', fontsize=13,)
(subsetdata.groupby('region')['Total Volume'].agg('sum')/len(data)).plot.bar(figsize=(24,10), colormap='Dark2', fontsize=13,)
plt.xlabel('region')
plt.ylabel('Total Volume')
plt.title('Bar Chart showing the total consumption in different region')


# #### Looks like these regions are where avacado consumption is very high
#  * West
#  * California
#  * SouthCentral
#  * Northeast
#  * Southeast

# ### Q.6 How price is distributed over the date column?

# In[39]:


byDate= data.groupby('Date').mean()
byDate['AveragePrice'].plot(kind='line', figsize=(15, 7), color='black')
plt.ylabel('AveragePrice')
plt.title('Linear Chart showing the variation of Average price over period of time')
#plt.legend(['Cholestrol (in mg)', 'Total_Fat (in g)'])


# In[ ]:





# ### Q.7 In which year and for which region was the Average price the highest?

# In[41]:


g=sns.factorplot('AveragePrice','region',data=data,
                   hue='year',
                   size=18,
                   aspect=0.7,
                   palette='Blues',
                   join=False,
              )
print(g)


# - Looks like there was a huge increase in Avocado prices as the demand was little high in Year 2017 in SanFranciso region. If you'll search it on google, you'll find the same.

# ### Q.8 How dataset features are correlated with each other?
# - Droping column name 4046,4225,4770 as I am not sure what these columns contribute in the data set.

# In[33]:


newdata=data.drop('4046', axis=1, inplace=False)
newdata1=newdata.drop('4225',axis=1, inplace=False)
newdata2=newdata1.drop('4770',axis=1, inplace=False)

corr_mat = newdata2.corr()
plt.figure(figsize=(10,8))
sns.heatmap(corr_mat, annot=True, cmap='viridis')


# - As we can see from the heatmap above, all the Features are not correleted with the Average Price column, instead most of them are correlated with each other. 

# ---
# <a name = Section9></a>
# # **9. Summarization**
# ---

# - Though lots of people are more likely to buy organic foods as it does not contain pesticides but Avocados are another piece of produce that do not warrant the organic label. Avocados have a naturally protective peel that keeps the fruit inside safe from toxins in the air.
# - What could be the region where consumtion is high does not have average price high for those region? High Pricing may include various factors such as transportaion charges etc. 
# - There are few states were Average price is high compare to other states but then also people are tend to buy avocado at higher price. such as LA, Great Lake etc.

# <a name = Section91></a>
# ### **9.1 Conclusion**
# 
# - Avocado is becoming trending food all over the world, so there should be enough supply as the demand goes up. Also we should focus on planting avocado trees in other parts of America too. As 90 % of avacado comes from Mexico. 
# - American should learn what techniques Mexicans are using to produce these high quality plants and they can apply the same .  By doing this the supply of avocados can be increase and price might go low comparatively.
# - Thre should be more supply in states such as LA and Great Lake .

# In[ ]:




