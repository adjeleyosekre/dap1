import streamlit as st
import pandas as pd
import plotly.express as px

def formatIndex(df):
    df['S/No.'] = range(1, len(df) + 1)
    df = df.set_index('S/No.')
    return df

df=pd.read_csv('superstore_data.csv',encoding='latin1') ##reading our data
st.write(df.head())
product_list=df['Product Name'].unique

total_sales_product=df[['Product Name','Sales']].groupby('Product Name').agg({'Sales':'sum'}).reset_index().sort_values(by='Sales',ascending=False)
st.dataframe(total_sales_product.head())
##st.dataframe(total_sales_product,2)
total_sales_product['Sales']=round(total_sales_product['Sales'],2)
total_sales_product=formatIndex(total_sales_product)
fig=px.bar(total_sales_product,x='Product Name',y='Sales')
st.plotly_chart(fig,use_container_width=True)
##add the format index option
