import pandas as pd
import numpy as np
import streamlit as st
from matplotlib import pyplot as plt


st.sidebar.image('https://upload.wikimedia.org/wikipedia/en/thumb/8/84/Indian_Premier_League_Official_Logo.svg/1200px-Indian_Premier_League_Official_Logo.svg.png')

st.title('**IPL  Analysis**')
user_menu=st.sidebar.radio('Select a option',
                 ('IPL Matches','Batsmen Statistics','Players'))

df=pd.read_csv("matches.csv")
dfb=pd.read_csv("most_runs_average_strikerate.csv")
dfp=pd.read_csv("Players.csv")
df.drop(columns=['umpire1','umpire2','umpire3'],inplace=True)
sea=df.groupby('Season')
ipl_winner=sea['winner'].value_counts()
year=df['Season'].sort_values().unique()
year_select=year.tolist()
year_select.insert(0,'Overall')
if user_menu=='IPL Matches':
    st.sidebar.header('IPL Matches')
    selected_year=st.sidebar.selectbox('Select Year',year_select)
      

#--------------------------------------------------


    if selected_year =='Overall':  
        col1,col2,col3=st.columns(3)
        with col1:
            st.header("Matches")
            st.title('786')
        with col2:
            st.header("Participated Teams")
            st.title('15')
        with col3:
            st.header("Most Championship Wins ")
            st.title('Mumbai Indians')
        col1,col2,col3=st.columns(3)
        with col1:
            st.header("Participating Country")
            st.title('11')
        with col2:
            st.header("Participated Players")
            st.title('566')
        with col3:
            st.header('Business value')
            st.title('$ 5.7 billion')
        st.write('---')
        st.write('**Match Wins**')
        for i in year:
            st.write(i)
            st.table(ipl_winner[i])
            st.write('---')
##---------------------------------------------------  
    if selected_year !='Overall':
        st.title(selected_year)
        ipl_matches=df.drop(columns=['id','city','toss_winner','toss_decision','result','dl_applied'])
        team=ipl_matches[ipl_matches['Season']==selected_year].tail(1)
       
       
        col1,col2=st.columns(2)
        with col1:
            st.header('Winner')
            st.title(team['winner'].tolist())    
        with col2:
            st.header('Man Of The Match')
            st.title(team['player_of_match'].tolist())
        
       
        st.table(ipl_matches[ipl_matches['Season']==selected_year])
##--------------------------------------------------------ipl_matches
elif user_menu=='Batsmen Statistics':
        dfb.drop(columns=['Out','Numberofballs'],inplace=True)
        dfb['Average']=round(dfb['Average'],2)
        dfb['Strikerate']=round(dfb['Strikerate'],2)
        N=list(range(1,517))
        dfb['N']=N
        dfb.set_index('N',inplace=True)
        st.header('Top 25 Batsmen')
        st.table(dfb.head(25))
        #----------graph
        st.title('Top 5 Batsmen')
        st.header('Batsman vs Total Runs')
        plt.style.use('fivethirtyeight')
        plt.figure(figsize=(10,5))
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.bar(dfb['Batsman'].head(5),dfb['Total_runs'].head(5),alpha=0.5,width=0.5)
        st.pyplot()
        #-----------
        st.header('Batsman vs Average')
        plt.style.use('fivethirtyeight')
        plt.figure(figsize=(10,5))
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.bar(dfb['Batsman'].head(5),dfb['Average'].head(5),alpha=0.5,width=0.5)
        st.pyplot()
        #--------------
        st.header('Batsman vs Strike Rate')
        plt.style.use('fivethirtyeight')
        plt.figure(figsize=(10,5))
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.bar(dfb['Batsman'].head(5),dfb['Strikerate'].head(5),alpha=0.5,width=0.5)
        st.pyplot()
#----------------------------------------player
if user_menu=='Players':
    dfp.drop(columns=['DOB'],inplace=True)
    dfp.set_index('Player_Name',inplace=True)
    country_select=['Select','India', 'England', 'South Africa', 'Australia', 'Bangladesh',
                    'Sri Lanka', 'West Indies', 'New Zealand', 'Pakistan',
                     'Netherlands', 'Zimbabwea']
    selected_country=st.sidebar.selectbox('Select Country',country_select)
    if selected_country=='Select':
        st.title('Select Country')
    else:
        st.title(selected_country)
        st.header('Players')
        st.table(dfp[dfp['Country']==selected_country])
        
      
        
    
    
