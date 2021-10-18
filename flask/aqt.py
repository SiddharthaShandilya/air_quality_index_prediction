from flask import Flask, render_template
from flask_cors import cross_origin
from src.utils.all_utils import read_yaml, create_directory, load_model, error_value
import sklearn
import pickle
import pandas as pd
import os, argparse

app = Flask(__name__)

@app.route("/aqt_predict")
def aqt_predict():
    return "<p>model fetched</p>"


@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")

if __name__ == "__main__":
    
    app.run(debug=True)
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="config/config.yaml")
    parsed_args = args.parse_args()
    config_path=parsed_args.config

    config = read_yaml(parsed_args.config)

    artifacts_dir = config["artifacts"]["artifacts_dir"]
    model_dir = config["artifacts"]["model"]["model_dir"]
    saved_model_filename = config["artifacts"]["model"]["xgboost_reg"]
    saved_model_file_path = os.path.join(artifacts_dir, model_dir, saved_model_filename)
    model = load_model(saved_model_file_path)

    print( " model loaded")

    aqt_predict(model)
    