import requests
from requests import HTTPError
from tkinter import *

API_KEY = "83a31d958b184d03bcb174115233110"

url = "http://api.weatherapi.com/v1/current.json"

root = Tk()
root.title("Weather App")
root.geometry("400x400")
root.resizable(0, 0)

city_name = StringVar()


def get_weather():
    city = city_name.get()
    payload = {'key': API_KEY, 'q': city, 'aqi': "no"}
    weather_request = requests.get(url, params=payload)
    weather_json = weather_request.json()

    tfield.delete("1.0", "end")

    if weather_request.status_code == 200:
        time_in_city = weather_json['location']['localtime']
        celcius = weather_json['current']['feelslike_c']
        general_weather = weather_json['current']['condition']['text']
        weather = f"The weather in the city of {city} is {general_weather}\n" \
                  f"It feels like {celcius} celcius outside\n" \
                  f"Time is {time_in_city}\n"
    else:
        weather = "No such city exists"

    tfield.insert(INSERT, weather)


city_label = Label(root, text="Enter City", font='Arial 12 bold').pack()
input_city = Entry(root, textvariable=city_name, width=24, font="Arial 14 bold").pack()

search_button = Button(root, command=get_weather, text="Show Weather", font='Arial 10',
                       bg='lightblue', fg='black', activebackground="teal",
                       padx=5, pady=5).pack(pady=20)

current_weather = Label(root, text="The Weather:", font='Arial 12 bold').pack()

tfield = Text(root, width=46, height=10)
tfield.pack()

root.mainloop()
