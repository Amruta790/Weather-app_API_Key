import requests

city_name = "Solapur"
API_key ="1ab654ea94d29ebe189fafb05fe1e3f2"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print("weather is", data["weather"][0]["description"])
    print("current temp is", data["main"]["temp"])
    print("current temp feels like is", data["main"]["feels_like"])
    print("humidity is", data["main"]["humidity"])
