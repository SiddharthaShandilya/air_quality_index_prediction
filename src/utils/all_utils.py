import yaml
import os
import json
import pandas as pd
import matplotlib.pyplot as plt



#-------------------------------------------------------------------------------
#   read_yaml
#-------------------------------------------------------------------------------

def read_yaml(path_to_yaml: str) -> dict:
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)

    return content



#-------------------------------------------------------------------------------
#   create_directory
#-------------------------------------------------------------------------------

def create_directory(dirs: list):
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
        print(f"directory is created at {dir_path}")


#-------------------------------------------------------------------------------
#   save_local_df
#-------------------------------------------------------------------------------

def save_local_df(data, data_path, index_status=False):
    data.to_csv(data_path, index=index_status)
    print(f"data is saved at {data_path}")



#-------------------------------------------------------------------------------
#   save_reports
#-------------------------------------------------------------------------------

def save_reports(report: dict, report_path: str, indentation=4):
    with open(report_path, "w") as f:
        json.dump(report, f, indent=indentation)
    print(f"reports are saved at {report_path}")



#-------------------------------------------------------------------------------
#   avg_data
#-------------------------------------------------------------------------------

def avg_data(aqi_data_dir_path,year):
    
    temp_i=0
    average=[]
    for rows in pd.read_csv("{}/aqi{}.csv".format(aqi_data_dir_path,year), chunksize=24):
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