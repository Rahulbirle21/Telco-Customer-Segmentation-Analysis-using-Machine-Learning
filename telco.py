import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas_bokeh
import os
import streamlit as st
from scipy.stats.stats import pearsonr

st.set_page_config(layout='wide')



st.title(':blue[Telco] Company Customer Segmentation Analysis :chart: :bar_chart:')
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

os.chdir(r'C:\Users\birle\NextHikes 5 Telco')
df = pd.read_csv('Telco customer satisfaction.csv')
num = list(df.select_dtypes(include='float64').columns)

st.sidebar.markdown('Select options to check correlation')
x_axis = st.sidebar.selectbox('Option1',num,index=0)
y_axis = st.sidebar.selectbox('Option2',num,index=1)



st.sidebar.markdown('### Data Consumption by Top 10 satisfied customers on different platforms')
top_sf = df.nlargest(10,['Satisfaction score'])
top_sf_col = ['MSISDN/Number']
bar = st.sidebar.selectbox('Select Customer ID',top_sf['MSISDN/Number'].values.tolist())


container = st.container()
chart1, chart2 = container.columns(2)

with chart1:
    fig,ax = plt.subplots()
    sns.scatterplot(x=x_axis,y=y_axis,data=df,)
    st.pyplot(fig,use_container_width=True)


with chart2:
    st.header('Data consumption on different platforms')
    st.bar_chart(top_sf,x='MSISDN/Number',y=['Total youtube(bytes)','Total netflix(bytes)','Total gaming(bytes)','Total social media(bytes)'],height=400,color=['#ff2b2b','#faca2b','#0068c9','#09ab3b'],use_container_width=True)



st.subheader('Top 10 handsets used by the customers')
fig1,ax = plt.subplots()
top_handsets = df['Handset Type'].value_counts().head(10)
sns.barplot(x=top_handsets.values,y=top_handsets.index,)
st.pyplot(fig1)

most_frequent_customers = df['MSISDN/Number'].value_counts().head(10)
st.subheader('Top 10 customers based on session frequency')
fig2,ax = plt.subplots()
sns.barplot(x=most_frequent_customers.index,y=most_frequent_customers.values)
plt.xticks(rotation=90)
st.pyplot(fig2)

top_duration_customer = df.nlargest(10,['Dur. (ms)'])
top_duration_customer = top_duration_customer[['Dur. (ms)','MSISDN/Number']]
st.subheader('Top 10 customers based on time duration on various platforms')
fig3,ax = plt.subplots()
sns.barplot(x='MSISDN/Number',y='Dur. (ms)',data= top_duration_customer)
plt.title('Top customers based on time duration')
plt.ylabel('Time duration of the customers')
plt.xticks(rotation=90)
st.pyplot(fig3)

top_consum = df.nlargest(10,['Total data consumption'])
top_consum = top_consum[['MSISDN/Number','Total data consumption']]
st.subheader('Top 10 customers based on total data consumption')
fig4,ax = plt.subplots()
sns.barplot(x='MSISDN/Number',y='Total data consumption',data=top_consum)
plt.title('Top 10  customers based on data consumption')
plt.ylabel('Data consumed by top 10 customers')
plt.xticks(rotation=90)
st.pyplot(fig4)

top_sm = df.nlargest(10,['Total social media(bytes)'])
top_sm = top_sm[['MSISDN/Number','Total social media(bytes)']]
st.subheader('Top 10 customer using Social Media')
fig5,ax=plt.subplots()
sns.barplot(x='MSISDN/Number',y='Total social media(bytes)',data=top_sm)
plt.title('Top 10  customers based on social media usage')
plt.ylabel('Data consumed by top 10 social media users')
plt.xticks(rotation=90)
st.pyplot(fig5)

top_yt = df.nlargest(10,['Total youtube(bytes)'])
top_yt = top_yt[['MSISDN/Number','Total youtube(bytes)']]
st.subheader('Top 10 customers in youtube data usage')
fig6,ax=plt.subplots()
sns.barplot(x='MSISDN/Number',y='Total youtube(bytes)',data=top_yt)
plt.title('Top 10  customers using youtube')
plt.ylabel('Data consumed by top 10 youtube user')
plt.xticks(rotation=90)
st.pyplot(fig6)

top_g = df.nlargest(10,['Total gaming(bytes)'])
top_g = top_g[['MSISDN/Number','Total gaming(bytes)']]
st.subheader('Top 10 customers in gaming data usage')
fig7,ax=plt.subplots()
sns.barplot(x='MSISDN/Number',y='Total gaming(bytes)',data=top_g)
plt.title('Top 10  customers using in gaming')
plt.ylabel('Data consumed by top 10 gamers')
plt.xticks(rotation=90)
st.pyplot(fig7)

app_data = pd.DataFrame({
    'Applications':['Gaming','Youtube','Google','Netflix','Social Media','Email'],
    'Data Consumed(bytes)':[64550395439016,3396545039272,1171101989130,3394313609363,274239359454,338867605596]
})

app_data = app_data.nlargest(3,['Data Consumed(bytes)'])
st.subheader('Top 3 most used application/platforms by the customers')
fig8,ax=plt.subplots()
sns.barplot(x='Applications',y='Data Consumed(bytes)',data=app_data)
plt.title('Top 3 most used services')
plt.ylabel('Data consumed by top 3 used services')
st.pyplot(fig8)

c1 = df[df['Engagement clusters'] == 0]
c2 = df[df['Engagement clusters'] == 1]
c3 = df[df['Engagement clusters'] == 2]
c4 = df[df['Engagement clusters'] == 3]
st.subheader('Visual representation of Engagement Cluster')
fig9,ax=plt.subplots()
sns.scatterplot(x='Dur. (ms)',y='Total data consumption',data=c1,color='green')
sns.scatterplot(x='Dur. (ms)',y='Total data consumption',data=c2,color='red')
sns.scatterplot(x='Dur. (ms)',y='Total data consumption',data=c3,color='black')
sns.scatterplot(x='Dur. (ms)',y='Total data consumption',data=c4,color='blue')
plt.title('Customer segmentation through clustering')
plt.xlabel('Dur. (ms)')
plt.ylabel('Total data consumption')
st.write('Based on the scatterplot, the best performing clusters are Red cluster,followed by blue cluster,black cluster and green cluster')
st.pyplot(fig9)

d1 = df[df['Experience cluster'] == 0]
d2 = df[df['Experience cluster'] == 1]
d3 = df[df['Experience cluster'] == 2]
d4 = df[df['Experience cluster'] == 3]
st.subheader('Visual representation of Experience cluster')
fig10,ax=plt.subplots()
sns.scatterplot(x='Total TCP(bytes)',y='Total bearer TP(Kbps)',data=d1,color='green')
sns.scatterplot(x='Total TCP(bytes)',y='Total bearer TP(Kbps)',data=d2,color='red')
sns.scatterplot(x='Total TCP(bytes)',y='Total bearer TP(Kbps)',data=d3,color='black')
sns.scatterplot(x='Total TCP(bytes)',y='Total bearer TP(Kbps)',data=d4,color='blue')
plt.title('Customer segmentation based on experience')
plt.xlabel('Total TCP(bytes)')
plt.ylabel('Total bearer TP(Kbps)')
st.write('Based on the analysis,the best performing cluster are blue cluster followed by blue,green and red cluster')
st.pyplot(fig10)

top_sf = df.nlargest(10,['Satisfaction score'])
top_sf = top_sf[['MSISDN/Number','Satisfaction score']]
st.subheader('Top 10 Overall satisfied customers')
fig11,ax=plt.subplots()
sns.barplot(x='MSISDN/Number',y='Satisfaction score',data=top_sf)
plt.title('Top 10  satisfied customers')
plt.xlabel('MSISDN/Number')
plt.xticks(rotation=90)
plt.ylabel('Satisfaction score')
st.pyplot(fig11)





