import pandas as pd
import numpy as np
import streamlit as st
from matplotlib import pyplot as plt
import plotly.offline as pyo
pyo.init_notebook_mode()
import plotly.express as px


st.sidebar.image('https://upload.wikimedia.org/wikipedia/en/thumb/8/84/Indian_Premier_League_Official_Logo.svg/1200px-Indian_Premier_League_Official_Logo.svg.png')

st.title('**IPL  Analysis**')
st.write('---')
user_menu=st.sidebar.radio('Select a option',
                 ('IPL Matches','Batsmen Statistics','Bowler Statistics','Players'))

df=pd.read_csv("matches.csv")
dfb=pd.read_csv("most_runs_average_strikerate.csv")
dfp=pd.read_csv("Players.csv")
dfd=pd.read_csv("deliveries.csv")
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
        #----------------------------------------
        y=[2014,2015,2016,2017,2018,2019]
        v=[3.2,3.7,3.5,3.8,5.3,5.7]

        val=pd.DataFrame(data=y)
        val['valuation']=v
        val.rename(columns={0:'year'},inplace=True)
        fig=px.line(val,x='year',y='valuation')
        st.header('IPL Valuation(USD)')
        st.plotly_chart(fig)
        data={   'N'      :[1,2,3,4,5,6,7],
                 'Sponsor':['DLF','Pepsi','Vivo','Vivo','Dream11','Vivo','Tata'],
                 'Period':['2008–2012','2013–2015','2016–2017','2018–2019','2020','2021','2022–2023'],
                 'Estimated sponsorship fee':['US$5.0 million','US$9.9 million','US$12.5 million','US$55.1 million','US$27.8 millon',                                                    'US$55.1 million','US$37.6–44.5 million']
                  }
        st.header('Estimated sponsorship Fee')
        d=pd.DataFrame(data)  
        d.set_index('N',inplace=True)
        st.table(d)
        
        
        st.header('Match Wins')
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
        player_select=dfd['batsman'].unique().tolist()
        player_select.insert(0,'Overall')
        selected_player=st.sidebar.selectbox('Select Player',player_select)
        if selected_player=='Overall':
            
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
        else:
            st.title('Overall Run Scored')
            st.title(selected_player)
            batsman=dfd.groupby('batsman')
            val=(batsman.get_group(selected_player))['batsman_runs'].value_counts()
            val.sort_index(inplace=True)
            st.table(val)
#-----------------------------------------bowler
elif user_menu=='Bowler Statistics':
    bowler_select=dfd['bowler'].unique().tolist()
    bowler_select.insert(0,'Overall')
    selected_bowler=st.sidebar.selectbox('Select Player',bowler_select)
    bowler=dfd.groupby('bowler')
    if selected_bowler=='Overall':
        st.title('Top 20 Bowler')
        st.header('Overall Wicket Taken')
        st.table((bowler['player_dismissed'].count()).sort_values(ascending=False).head(20))
    else:
        st.title('Bowler Statistics')
        st.write('---')
        col1,col2=st.columns(2)
        with col1:
            st.header('Bowler')
            st.title(selected_bowler)
        with col2:
            st.header('Wicket Taken')
            st.title((bowler.get_group(selected_bowler))['player_dismissed'].count())
        
    

            
            
            
            
#----------------------------------------player
elif user_menu=='Players':
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
        
      
        
    
    
