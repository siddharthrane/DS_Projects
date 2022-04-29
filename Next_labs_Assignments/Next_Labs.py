# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 08:10:58 2022

@author: New
"""

import streamlit as st
import pandas as pd


def main():
    
    st.subheader("Dataset")
    data_file = st.file_uploader("Upload CSV",type=["csv"]) #displaying a file uploader widget
		
    if data_file is not None:
        #will retreive the file details
        file_details = {"filename":data_file.name, "filetype":data_file.type,"filesize":data_file.size}
        st.write(file_details) #printing out the file details
        df=pd.read_csv(data_file) #reading the input csv file
        st.dataframe(df)  #printing the dataframe
        df_info=df.loc[(df.Text.str.contains("Good|Nice|Fantastic|Great")) &
               (df.Star==1) &
               (df['User Name']),['Text','Star','User Name']
               ]
        #df_info will extract the data with positive review text but negative rating
        st.subheader("Reviews with positive review text but negative rating:")
        st.dataframe(df_info)

#performing Authentication using hardcoded pass

password=st.text_input("Password:", value="", type="password") 
if password!='data' and password!='':
    st.subheader('Incorrect password!')
    
elif password=='data':
    main()


    