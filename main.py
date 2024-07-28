import requests
import tkinter as tk
from tkinter import messagebox

def get_weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def show_weather():
    api_key = '8e7735c4e1ca01cab8259ab442bab77a'
    city = city_entry.get()

    data = get_weather(city, api_key)

    if data and data.get('cod') == 200:
        weather = data['weather'][0]['main']
        temp = round(data['main']['temp'])
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        result_label.config(text=f"Weather in {city}: {weather}\n"
                                 f"Temperature: {temp}ºF\n"
                                 f"Humidity: {humidity}%\n"
                                 f"Wind speed: {wind_speed} mph")
    else:
        messagebox.showerror("Error", "City not found or an error occurred.")

root = tk.Tk()
root.title("Weather App")

city_label = tk.Label(root, text="Enter city name:")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

get_weather_button = tk.Button(root, text="Get Weather", command=show_weather)
get_weather_button.pack()

result_label = tk.Label(root, text="", justify="left")
result_label.pack()

root.mainloop()
