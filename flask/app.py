from flask import Flask, render_template, request
from flask_cors import cross_origin
from src.utils.all_utils import read_yaml, create_directory, load_model, error_value
import os

#config_path="config/config.yaml"
config = read_yaml("config/config.yaml")
artifacts_dir = config["artifacts"]["artifacts_dir"]
model_dir = config["artifacts"]["model"]["model_dir"]
saved_model_filename = config["artifacts"]["model"]["xgboost_reg"]
saved_model_file_path = os.path.join(artifacts_dir, model_dir, saved_model_filename)
model = load_model(saved_model_file_path)
print(" model loaded")

app = Flask(__name__)



@app.route("/aqt_predict",methods = ["GET", "POST"])
def aqt_predict():
  

    if request.method == "POST":
        '''
        T = request.form["Average_temperature"] 
        TM = request.form["Maximum_temperature"]
        Tm = request.form["Minimum_temperature"]
        SLP = request.form["Atmospheric_pressure_at_sea_level"]
        H = request.form["Average_humidity"]
        VV = request.form["Average_visibility"]
        V = request.form["Average_wind_speed"]
        VM = request.form["Maximum_wind_speed"]
        '''

        output = model.predict([[7.4,9.8,4.8,1017.6,93.0,0.5,4.3,9.4]])
        
        return "<p>model fetched from {}</p>".format(output)


@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")

if __name__ == "__main__":
    aqt_predict()
    app.run(Debug=True)
    