import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
a=st.sidebar.radio("Navigation",['Home','Data Analysis','About us'])
if a=='Home':
    st.title("Wellcome")
    st.header("hello.Please enter your preffered action from below.")
    st.image('istockphoto-1010491174-612x612.jpg')
elif a=='Data Analysis':
    st.title("Welcome to the Data Analysis section")
    b=st.file_uploader("Please enter your csv file")
    if b is not None:
        data=pd.read_csv(b)
    if b is not None:
        c,d,e,f,g=st.tabs(['DataFrame',"columns",'datatypes','size','plot'])
        with c:
            st.dataframe(data)
        with d:
            st.write(data.columns)
        with e:
            st.write(data.dtypes)
        with f:
            st.write(data.shape)
        with g:
            cols=data.select_dtypes(['int64','float64'])
            cols=cols.keys()
            x=st.selectbox("Please selet the x cordinate column name",cols)
            st.write(x)
            y=st.selectbox("Please select the y cordinate column name ",cols)
            st.write(y)
            z=st.selectbox("please select a plotting function",['Line plot','scatter plot','bar plot'])
            st.write(z)
            gen=st.button("Generate Plot")
            if gen:
                if z=='Line plot':
                    fig,ax=plt.subplots()
                    ax.plot(data[x],data[y])
                    ax.set_xlabel(x)
                    ax.set_ylabel(y)
                    st.pyplot(fig)
                elif z=="scatter plot":
                    fig,ax=plt.subplots()
                    ax.scatter(data[x],data[y])
                    ax.set_xlabel(x)
                    ax.set_ylabel(y)
                    st.pyplot(fig)
                elif z=='bar plot':
                    fig,ax=plt.subplots()
                    ax.bar(data[x],data[y])
                    ax.set_xlabel(x)
                    ax.set_ylabel(y)
                    st.pyplot(fig)
elif a=='About us':
    st.title("Md Naimur Asif Borno")
    st.header("Department of Mechatronics Engineering")
    st.header("Rajshahi University of Engineering & Technology")
    st.header("+8801860460298")
                
                


        
    
    
    



    

