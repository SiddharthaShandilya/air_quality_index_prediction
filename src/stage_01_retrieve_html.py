import os
import time
import requests
import sys
from src.utils.all_utils import *

def retrieve_html():
    
    #we are going to fetch every month's data from year 2103 to 2020
    for year in range(2013,2019):
        for month in range(1,13):
            
            if month<10:
                url="https://en.tutiempo.net/climate/0{}-{}/ws-421820.html".format(month, year)
                
            else:
                 url="https://en.tutiempo.net/climate/{}-{}/ws-421820.html".format(month, year)
                 
            text = requests.get(url)
            text_utf = text.text.encode('utf-8')
        
            if not os.path.exists("artifacts/data/Html_Data/{}".format(year)):
                
                        
                os.makedirs("artifacts/data/Html_Data/{}".format(year))
                
            with open("artifacts/data/Html_Data/{}/{}.html".format(year,month),"wb") as output:
                
                output.write(text_utf)

            print("artifacts/data/Html_Data {} / {} created".format( year, month))
                  
    sys.stdout.flush()
    
if __name__=="__main__":

    start_time=time.time()
    retrieve_html()
    stop_time=time.time()
    print("time taken{}".format(stop_time-start_time))