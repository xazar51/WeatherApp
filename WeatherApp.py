import requests

API_KEY = "83a31d958b184d03bcb174115233110"

user_input = input("Please enter the city in which you'd like to know the weather?\n")

url = "http://api.weatherapi.com/v1/current.json"
payload = {'key': API_KEY, 'q': user_input, 'aqi': "no"}

weather_request = requests.get(url, params=payload)
weather_json = weather_request.json()

if weather_request.status_code == 200:
    print(f"The weather in the city of {weather_json['location']['name']} is :\n"
          f"The time is {weather_json['location']['localtime']}\n"
          f"The weather is : {weather_json['current']['condition']['text']}, "
          f"it feels like {weather_json['current']['feelslike_c']} Celcius")
else:
    print("Most likely you've entered a wrong city name")
