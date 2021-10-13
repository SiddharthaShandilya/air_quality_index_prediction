# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 09:10:42 2021

@author: gg415
"""


import pandas as pd
import matplotlib.pyplot as plt

import os
import csv

#from stage_02_aqt_data_processing import avg_data
from src.utils.all_utils import avg_data
import requests
import sys 
from bs4 import BeautifulSoup


#_____________________________________________________________________________
#
#          Extracting Data From Beautiful Soup
#_____________________________________________________________________________


def met_data(month, year):
    file_html=open('artifacts/data/Html_Data/{}/{}.html'.format(year,month),'rb')
    plain_text = file_html.read()

    print("-"*10 + " META_DATA" + "-"*10)
    tempd=[]
    finald=[]
    
    soup = BeautifulSoup(plain_text,'lxml')
    
    for table in soup.findAll("table",{"class":"medias mensuales numspan"}):
        for tbody in table:
            for tr in tbody:
                a = tr.get_text()
                tempd.append(a)
                
                
    #print(type(tempd))
                
    rows = len(tempd)/15
    
    
    
    for times in range(round(rows)):
        newtempd=[]
        for i in range(15):
            newtempd.append(tempd[0])
            tempd.pop(0)
            
        finald.append(newtempd)
        #print(finald)
        
        
        
    length = len(finald)

    print(" length of finald = > {} ".format(length))
    print( " month = > {} || year => {}".format(month, year))
    
    finald.pop(length-1)  # removing the last row which contains mean and mode

    finald.pop(0)  # removing the first row which contains all the columns name
    
    
    # removing the columns with null values
    for a in range (len(finald)):
        
        finald[a].pop(6) # now that we have poped 6th first so the entire column alignment needs to be changed accordingly
        finald[a].pop(13)# 15th columns
        finald[a].pop(12) # 14th column
        finald[a].pop(11) # 13th column
        finald[a].pop(10) # 12th column
        finald[a].pop(9) # 11th column
        finald[a].pop(3) # 4th column is not present
        finald[a].pop(0) # removing column 1st because removing 6th column does not affect 0th position
    
    #print(finald)    
    return finald




#_____________________________________________________________________________
#
#           Combining data
#_____________________________________________________________________________

def data_combine(year, cs):
    
    for a in pd.read_csv('artifacts/data/Real-Data/real_'+str(year)+'.csv',chunksize=cs):
        
        print("-"*30 + " data_combine" + "-"*30)
        print(a)
        print("-"*30 + " data_combine" + "-"*30)
    
        df = pd.DataFrame(data=a)
        mylist = df.values.tolist()
    
    print("-"*30 + " data_combine_my_list" + "-"*30)
    print(mylist)   
    print("-"*30 + " data_combine_my_list" + "-"*30)
    return mylist

#_____________________________________________________________________________
#
#           Main Function
#_____________________________________________________________________________


if __name__ == "__main__":
    
    if not os.path.exists('artifacts/data/Real-Data/'):
        os.makedirs('artifacts/data/Real-Data/')
    for year in range(2013, 2017):
        final_data=[]
        with open('artifacts/data/Real-Data/real_'+ str(year) + '.csv','w') as csvfile:
            wr = csv.writer(csvfile, dialect='excel')
            wr.writerow(
                ['T', 'TM', 'Tm', 'H', 'VV', 'V', 'VM', 'PM 2.5'])   
        
        for month in range(1,13):
            temp = met_data(month, year)         
            final_data = final_data + temp
        
        pm = avg_data(year)

        if len(pm) == '364':
            pm.insert(364,'_')

        for i in range (len(final_data)-1):
            final_data[i].insert(8,pm[i])


            
        with open('artifacts/data/Real-Data/real_'+ str(year) + '.csv', 'a') as csvfile:

            wr = csv.writer(csvfile, dialect='excel')
            for row in final_data:
                flag = 0
                for elem in row:
                    if elem == "" or elem == "-":
                        flag = 1
                if flag == 1:
                    wr.writerow(row)
                    print("-"*30 + " real_data_row" + "-"*30)
                    print(row)
                    print("-"*30 + " real_data_row" + "-"*30)
                       
                    
    print("-"*30 + " real_data_wr.head" + "-"*30)
    print(pd.read_csv("artifacts/data/Real-Data/real_{}.csv".format(year)))
    print("-"*30 + " real_data_wr.head" + "-"*30)   

    data_2013 = data_combine(2013, 600)
    data_2014 = data_combine(2014, 600)
    data_2015 = data_combine(2015, 600)
    data_2016 = data_combine(2016, 600)
    #data_2017 = data_combine(2017, 600)
    #data_2018 = data_combine(2018, 600)
     
    total=data_2013+data_2014+data_2015+data_2016 #+data_2017+data_2018
    
    #print("-"*20 + " total " + "-"*20)
    #print(total)  
    #print("-"*20 + " total " + "-"*20)    

    with open('artifacts/data/Real-Data/Real_Combine.csv', 'w') as csvfile:
        wr = csv.writer(csvfile, dialect='excel')
        wr.writerow(
            ['T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
        wr.writerows(total)
        


df=pd.read_csv('artifacts/data/Real-Data/Real_Combine.csv')
print(df.head())



