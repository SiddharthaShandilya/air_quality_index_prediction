import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import metrics
import os
import time 
import argparse
import requests
import sys
from src.utils.all_utils import create_directory, read_yaml
from sklearn.ensemble import ExtraTreesRegressor

def eda(real_data_combined_file_path):

    df = pd.read_csv("../artifacts/data/Real-Data/Real_Combine.csv")
    df.dropna(inplace= True)
    X = df.iloc[:,:-1] # removing the last column
    y = df.iloc[:,-1]

    # finding co- relation

    corr_mat = df.corr()
    top_corr_features = corr_mat.index
    print("top_corr_features = {}".format(top_corr_features))

    # feature importance

    
    model = ExtraTreesRegressor()
    model.fit(X,y)
    print(model.feature_importances_)

def splitting_data(real_data_combined_file_path)



if __name__=="__main__":

    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config/config.yaml")

    parsed_args = args.parse_args()

    config_path=parsed_args.config

    config = read_yaml(config_path)
    

    artifacts_dir = config["artifacts"]['artifacts_dir'] # points to artifacts folder
    data_local_dir = config["artifacts"]['data_local_dir'] # points to data folder inside artifacts
    real_data_dir = config["artifacts"]['real_data_dir'] # points to Real-Data folder inside artifacts/data
    real_data_combined_file = config["artifacts"]['real_data_combined_file'] # points to  Real_Combine.csv file inside artifacts/data/Real-Data

    

    data_local_dir_path = os.path.join(artifacts_dir, data_local_dir)
    
    real_data_dir_path = os.path.join(data_local_dir_path, real_data_dir)

    real_data_combined_file_path = os.path.join(real_data_dir_path, real_data_combined_file)

    print("#"*20 + " real_data_combined_file_path " + "#"*20)
    print(" real_data_dir_path = {}".format(real_data_dir_path))
    print(" real_data_combined_file_path = {}".format(real_data_combined_file_path))
    print("#"*20 + " real_data_combined_file_path " + "#"*20)
  
    eda(real_data_combined_file_path)