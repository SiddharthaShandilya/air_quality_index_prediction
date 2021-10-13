# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 13:54:52 2021

@author: gg415

import pandas as pd
import matplotlib.pyplot as plt

def avg_data(year):
    
    temp_i=0
    average=[]
    for rows in pd.read_csv("./data/AQI/aqi{}.csv".format(year), chunksize=24):
#    for rows in pd.read_csv("data/AQI/aqi2014.csv", chunksize=24):

        add_var=0
        data=[]
        avg=0.0
        df=pd.DataFrame(data=rows)
        for index, rows in df.iterrows():
            data.append(rows['PM2.5'])
            #count=
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
                    #count=count+1
            elif type(i) is str:
                if i!="NoData" and i!="PwrFail" and i!="---" and i!="InVld":
                    temp=float(i)
                    add_var=add_var+temp
                    #count=count+1
        avg = add_var/24   #count
        temp_i=temp_i+1
        average.append(avg)
    return average
            
            
if __name__=="__main__":
    list2013=avg_data("2013")
    list2014=avg_data("2014")
    list2015=avg_data("2015")
    list2016=avg_data("2016")
    list2017=avg_data("2017")
    list2018=avg_data("2018")
    
    print(list2013)
    '''
    plt.plot(range(0,365), list2013, label="2013DATA")
    plt.plot(range(0,364), list2014, label="2014DATA")
    plt.plot(range(0,365), list2015, label="2015DATA")
    #plt.plot(range(0,365),list2016, label="2016DATA")
    #plt.plot(range(0,365),list2017, label="2017DATA")
    #plt.plot(range(0,365),list2018, label="2018DATA")
    
    plt.xlabel('Day')
    plt.ylabel('PM2.5')
    plt.legend(loc="upper right")
    
    plt.show()
    '''
    
    
            

 """