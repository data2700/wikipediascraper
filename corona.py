#!/usr/bin/python
# encoding: utf-8
import sys
# sys.setdefaultencoding('UTF16')
import pandas as pd
import numpy as np
import wikipedia as wp
import time

def executeSomething():    #if you don't have access to CRON everything that follows this line will run in a timer
                           #you can decide the time by entering it at the bottom.  Its not exact, but close enough for
                           #my purposes

    html = wp.page("2020_coronavirus_outbreak_in_Sweden").html().encode("UTF-16") # page to be scraped
    try:                   #the number in the [] is the table on the wikipedia page.  There can be more than one
                           #so search the html source for  the word: wikitable to find out which table is yours
                           #change the number until you get the right once scraped
                           
        #df = pd.read_html(html)[1]  # Try 2nd table first as most pages contain contents table first
        df = pd.read_html(html,header=0)[2]  # Try 2nd table first as most pages contain contents table first
        #df = pd.read_html(html)[1]  # Try 2nd table first as most pages contain contents table first

        tables = pd.read_html(html,header=0)[2]
    except IndexError:
        df = pd.read_html(html)[2]
    #print(df.to_string())
    #df=pd.DataFrame(A,columns=['Case no.'])
    #df['Date announced']=B
    #df['Origin type']=C
    #df['Origin']=D
    #df['Location']=E
    #df['Treatment facility']=F
    #df['Sex']=G
    #df['Age']=H
    #df['City']=I
    #df['Region']=J
    df.index.name = 'foo'    #rename the first index to 'foo' or whatever you'd like. this is optional
    df                       # this code was originally in a jupyter notebook and in that format it is useful to show the
                             # dataframe
    #df.rename(columns={'Location.1':'Location1'}, inplace=True)

    #df['Location1'] = df['Location1'].replace({'VGR':'VastraGotaland'})
    #df['Location.1'] = df['Location.1'].replace({'VGR':'VastraGotaland', 'r':'responsive'})

    df.drop(df.index[[0]],inplace=True)          #different manipulations of the dataframe index. this is optional
    df.drop(df.index[[1]],inplace=True)
    df.reset_index(drop=True,inplace=True)

    df.index.name = 'foo'      #rename the first index to 'foo' or whatever you'd like. this is optional
    df.index = np.arange(1, len(df)+1)
    #read_file = df
    df.to_csv('corona.csv',index=True, header = True, encoding='utf-8-sig')  #saving dataframe to a csv file 
    read_file = pd.read_csv ('corona.csv')                                   #reading the csv file that was just saved
    read_file.to_excel ('/var/www/corona.xlsx', index = None, header=True, encoding='utf-8-sig')  # saving the csv file to an excel file


    time.sleep(900)                        #Here you can set the amount of sleep time 60 = 1 minute 
    print('one time')                      #print a message to console after the program is completed
while True:                                #complete the while loop.  This is to get around scheduling a cron job. its a hack but a good one :) 
    executeSomething()                     #call the function again to run it all one more time  
