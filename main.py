import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# 0 configure the page
st.set_page_config(
    page_title="Data Science App",
    page_icon="🧊",
    layout="wide",
)



# 1  load the data 
@st.cache_data
def load_data():
    url = 'data/Top_rated_movies1.csv'
    df = pd.read_csv(url,parse_dates=['release_date'])
    return df






# 2 built the UI

st.title("Data Science App")
with st.spinner("loading..."):
    df=load_data()
st.header("IMDB 8000 movies dataset")
st.info("Raw data in Data frame")
st.dataframe(df,use_container_width=True)
st.success("Column informationthe dataset ")
cols =df.columns.tolist()
st.subheader(f'Total column {len(cols)}⏩ {",".join(cols)}')




# 3 add same graph and winget 
st.header("Basic Data Visulisation")
gop=['bar','line','area']

c1 ,c2 = st.columns(2)
sel_op = c1.selectbox("select the type of plot",gop)


if sel_op == gop[0]:
    subset = df.sort_values(by='popularity')[:50]
    fig = px.bar(subset,x='title',y='popularity',log_y=True)
elif sel_op == gop[1]:
    subset = df.sort_values(by='popularity')[:100]
    fig = px.bar(subset,x='title',y='popularity')
elif sel_op == gop[2]:
    subset = df.sort_values(by='popularity')[:100]
    fig = px.bar(subset,x='title',y='popularity')
elif sel_op == gop[3]:
    subset = df.sort_values(by='popularity')[:100]
    fig = px.bar(subset,x='title',y='popularity')
    c1.plotly_chart(fig,use_container_width=True)



    sel_op2 = c2.radio("select the type of plot for vote",gop)

    subset2 = df.sort_values(by='vote_count')[:50]

if sel_op2 == gop[0]:
    subset2 = df.sort_values(by='vote_count')[:50]
    fig = px.bar(subset2,x='title',y='vote_count')
elif sel_op2 == gop[1]:
    subset2 = df.sort_values(by='vote_count')[:100]
    fig = px.bar(subset2,x='title',y='vote_count')
elif sel_op2 == gop[2]:
    subset2 = df.sort_values(by='vote_count')[:100]
    fig = px.bar(subset2,x='title',y='vote_count')
elif sel_op2 == gop[3]:
    subset2 = df.sort_values(by='vote_count')[:100]
    fig = px.bar(subset2,x='title',y='vote_count')
c2.plotly_chart(fig,use_container_width=True)





# 4 Adjust layout

t1,t2,t3= st.tabs(["Bivariate","trivariate" ,'About'])
num_cols = df.select_dtypes(include=np.number).columns.tolist()
with t1:
    c1,c2 = st.columns(2)
    col1=c1.radio("select the first column for Scatter plot",num_cols)
    col2 = c2.radio("select the first column for Scatter plot",num_cols)
    fig = px.scatter(df,x=col2,y=col2,title=f'{col1}vs{col2}')
    st.plotly_chart(fig,use_container_width=True)
    with t2:
         c1, c2, c3 = st.columns(3)
    col1 = c1.selectbox("Select the first column for 3d plot", num_cols)
    col2 = c2.selectbox("select the second column for 3d plot", num_cols)
    col3 = c3.selectbox("select the third column for 3d plot", num_cols)
    fig = px.scatter_3d(df, x=col1, y =col2,z=col3,title=f'{col1} vs {col2} vs {col3}',
                        height=700)
    st.plotly_chart(fig,use_container_width=True)


# how to run app
# open terminal and run
# streamlit run main.py