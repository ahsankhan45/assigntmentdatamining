# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session
import pandas as pd
import numpy as np
import plotly
from plotly.offline import *
import plotly.offline as pyo
import plotly.graph_objs as go
import plotly.express as px
init_notebook_mode(connected = True)
data = pd.read_csv("/kaggle/input/bigbasket-entire-product-list-28k-datapoints/BigBasket Products.csv")
data
data.drop('index', axis = 1, inplace = True)
data.drop('description', axis = 1, inplace = True)
data.info()
data.isnull().sum()
# replacing NaN values with mean
data['rating'] = data['rating'].fillna(data['rating'].mean())
data.isnull().sum()
#dropping NaN product and brand row
data.dropna(how = 'any', inplace = True)
data.isnull().sum()
data['category'] = data['category'].astype("category")
data['sub_category'] = data['sub_category'].astype('category')
data['rating'] = data['rating'].astype('category')
data['brand']= data['brand'].astype('category')
data.info()
print(data['product'].nunique())
print(data['category'].nunique())
print(data['sub_category'].nunique())
print(data['brand'].nunique())
print(data['type'].nunique())
print(data['rating'].nunique())
categories = data['category'].drop_duplicates()
category_count_list = []
for category in categories:
    category_count = 0
    for ctg in data['category']:
        if category == ctg:
            category_count +=1
    category_count_list.append(category_count)

fig1 = go.Figure(data = go.Pie(labels = categories, values = category_count_list))
iplot(fig1)
products = data['product'].drop_duplicates()
product_gt10 = []
product_name_gt10 = []
product_gt7 = []
product_name_gt7 = []
product_gt5 = []
product_name_gt5 = []
product_ls5 = []
product_name_ls5 = []
for product in products:
    product_count = 0
    
    for prd in data['product']:
        if product == prd:
            product_count +=1
    
    if product_count >= 10:
        product_gt10.append(product_count)
        product_name_gt10.append(product)
    elif product_count < 10 and product_count >= 7:
        product_gt7.append(product_count)
        product_name_gt7.append(product)
    elif product_count < 7 and product_count >= 5:
        product_gt5.append(product_count)
        product_name_gt5.append(product)
    else:
        product_ls5.append(product_count)
        product_name_ls5.append(product)


#. more than 10 
fig2 = go.Figure(data = go.Bar(y = product_gt10, x = product_name_gt10 ),layout_title_text="Sold more than 10 Units")
iplot(fig2)

#more than 5 or equal to 5
fig3 = go.Figure(data = go.Bar(y = product_gt7, x = product_name_gt7 ),layout_title_text="Sold 7 to 9 Units")
iplot(fig3)
#less than 5
fig4 = go.Figure(data = go.Bar(y = product_gt5, x = product_name_gt5 ),layout_title_text="Sold 5 to 6 Units")
iplot(fig4)
print(f"No. of products sold less than 5 are:{len(product_name_ls5)}")
brands = data['brand'].drop_duplicates()
# more than or equal to 100
brand_gt100 = []
brand_name_gt100 = []
# from 70 to 99
brand_gt70 = []
brand_name_gt70 = []
#from 50 to 69
brand_gt50 = []
brand_name_gt50 = []
#from 30 to 49
brand_gt30 = []
brand_name_gt30 = []
# from 15 to 29
brand_gt15 = []
brand_name_gt15 = []
# less than 15
brand_ls15 = []
brand_name_ls15 = []
for brand in brands:
    brand_count = 0
    for brd in data['brand']:
        if brand == brd:
            brand_count +=1
            
    if brand_count >= 100:
        brand_gt100.append(brand_count)
        brand_name_gt100.append(brand)
    elif brand_count < 100 and brand_count >=70:
        brand_gt70.append(brand_count)
        brand_name_gt70.append(brand)
    elif brand_count < 70 and brand_count >=50:
        brand_gt50.append(brand_count)
        brand_name_gt50.append(brand)
    elif brand_count < 50 and brand_count >=30:
        brand_gt30.append(brand_count)
        brand_name_gt30.append(brand)
    elif brand_count < 30 and brand_count >=15:
        brand_gt15.append(brand_count)
        brand_name_gt15.append(brand)
    else:
        brand_ls15.append(brand_count)
        brand_name_ls15.append(brand)

fig5 = go.Figure(data = go.Bar(y = brand_gt100, x = brand_name_gt100 ),layout_title_text="Brands sold more than 100 Units")
iplot(fig5)

fig6 = go.Figure(data = go.Bar(y = brand_gt70, x = brand_name_gt70 ),layout_title_text="Brands sold 70 to 99 Units")
iplot(fig6)

fig7 = go.Figure(data = go.Bar(y = brand_gt50, x = brand_name_gt50 ),layout_title_text="Brands sold 50 to 69 Units")
iplot(fig7)

fig8 = go.Figure(data = go.Bar(y = brand_gt30, x = brand_name_gt30 ),layout_title_text="Brands sold 30 to 49 Units")
iplot(fig8)

fig9 = go.Figure(data = go.Bar(y = brand_gt15, x = brand_name_gt15 ),layout_title_text="Brands sold 15 to 29 Units")
iplot(fig9)

print(f"No. of brands selling less than 15 units are: {len(brand_ls15)}")

categories = data['category'].drop_duplicates()
graph_data = []
ratings_list = []
for category in categories:
    count = 0
    rating = 0
    
    for row in range(0,len(data)):
        if row in [9765,14363]:
            pass
        else:
            if category == data['category'][row]:
                rating += data['rating'][row]
                count +=1
                
    ratings_list.append(rating/count)

fig10 = go.Figure(data = go.Scatter(y = ratings_list, x = categories ),layout_title_text="Average rating according to the category")
iplot(fig10)

discount = []

for category in categories:
    sales = 0
    market = 0
    
    for row in range(0,len(data)):
        if row in [9765,14363]:
            pass
        else:
        
            if category == data['category'][row]:
                sales += data['sale_price'][row]
                market += data['market_price'][row]
    discnt = (market - sales)/market * 100       
    discount.append(discnt)
fig11 = go.Figure(data = go.Scatter(y = discount, x = categories ),layout_title_text="Average discount according to the category")
iplot(fig11)

fig12 = px.histogram(data, x = 'category', color = 'sub_category', title = 'Count of Subcategories for each category')
fig12.show()
fig13 = px.histogram(data, x = 'category', color = 'type', title = 'Count of type for each category')
fig13.show()
