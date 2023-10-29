from flask import Flask ,render_template ,request ,jsonify
import requests
app =Flask(__name__)


@app.route("/")
def Homepage():
    return render_template("index.html")

@app.route("/weatherapp",methods = ["POST" ,"GET"])
def get_weather():

    url ="https://api.openweathermap.org/data/2.5/weather"
    param ={
        "q" :request.form.get("city"),
        "appid":request.form.get("appid"),
        "unit":request.form.get("units")
    }
    response =requests.get(url ,params= param)
    data =response.json()
    return f"Data : {data}"

if __name__ == "__main__":
    app.run(host= "0.0.0.0" ,port =5000)