import requests
from flask import Flask,request,render_template
app=Flask(__name__)
#firstly api documentation ma apelu j hase ane postman ma run krine jovani pehla
def fetch_weather_data(city):
    API_KEY ="add_your_api_key"
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response=requests.get(url,timeout=5)
        data=response.json()
        weather_images ={
            "clear sky": "static/images/clear_sky.png",
            "few clouds": "static/images/few_clouds.png",
            "scattered clouds": "static/images/scattered_clouds.png",
            "rain": "static/images/rain.png",
            "thunderstorm": "static/images/thunderstorm.png",
            "snow": "static/images/snow.png",
            "mist": "static/images/mist.png"

        }
        image_url=weather_images.get( data['weather'][0]['description'])
        return{
        
        'temp': data['main']['temp'],
        'humidity':data['main']['humidity'],
        'city':data['name'],
        'speed':data['wind']['speed'],
        'country':data['sys']['country'],
        "image":image_url
        }
        
    except Exception as e:
        print(e)
@app.route('/',methods=['GET','POST'])
def index():
    weather=None
   
    if request.method == "POST":
        city_name = request.form["city"]
        weather = fetch_weather_data(city_name)

    return render_template("index.html", weather=weather)
if __name__ == "__main__":
    app.run(debug=True)
