from tkinter import *
from tkinter import ttk
from datetime import datetime
from timezonefinder import TimezoneFinder
import geopy
import requests
import pytz

part = 'minutely'
api_key = 'enter_api'

def get_weather_data(lat, lng):
    try:
        url = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lng}&exclude={part}&units=imperial&appid={api_key}'
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        temp = data.get('current', {}).get('temp')
        humidity = data.get('current', {}).get('humidity')
        precipitation_prob = data.get('hourly', [])[0].get('pop', 0) * 100 
        wind_speed = data.get('current', {}).get('wind_speed')
        return {
            "temp": f"{temp:.2f}°F" if temp is not None else "Temperature not available",
            "humidity": f"{humidity}%" if humidity is not None else "Humidity not available",
            "precipitation_prob": f"{precipitation_prob:.0f}%" if precipitation_prob is not None else "Precipitation data not available",
            "wind": f"{wind_speed} mph" if wind_speed is not None else "Wind data not available"
        }
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return {
            "temp": "Temperature not available",
            "humidity": "Humidity not available",
            "precipitation_prob": "Precipitation data not available",
            "wind": "Wind not available"
        }
    except ValueError as e:
        print(f"Error processing data: {e}")
        return {
            "temp": "Temperature not available",
            "humidity": "Humidity not available",
            "precipitation_prob": "Precipitation data not available",
            "wind": "Wind not available"
        }

def get_coordinates(location):
    try:
        geolocator = geopy.Nominatim(user_agent="weather_app")
        location = geolocator.geocode(location)
        if location:
            return location.latitude, location.longitude
        return None, None
    except geopy.exc.GeocoderServiceError as e:
        print(f"Geocoding failed: {e}")
        return None, None

def get_local_time(latitude, longitude):
    try:
        timezone_str = TimezoneFinder().timezone_at(lat=latitude, lng=longitude)
        if timezone_str is None:
            return "Time zone could not be determined."
        timezone = pytz.timezone(timezone_str)
        local_time = datetime.now(timezone)
        formatted_time = local_time.strftime('%I:%M %p')
        return formatted_time
    except Exception as e:
        print(f"Error getting local time: {e}")
        return "Time not available"

def show_data():
    location_name = location_entry.get()
    latitude, longitude = get_coordinates(location_name)
    if latitude is not None and longitude is not None:
        local_time = get_local_time(latitude, longitude)
        weather_data = get_weather_data(latitude, longitude)
        time_label.config(text=f"Local Time: {local_time}")
        temp_label.config(text=f"Temperature: {weather_data['temp']}")
        humidity_label.config(text=f"Humidity: {weather_data['humidity']}")
        precipitation_label.config(text=f"Precipitation: {weather_data['precipitation_prob']}")
        wind_label.config(text=f"Wind: {weather_data['wind']}")
    else:
        time_label.config(text="Invalid location")
        temp_label.config(text="")
        humidity_label.config(text="")
        precipitation_label.config(text="")
        wind_label.config(text="")

window = Tk()
window.geometry("800x800")

canvas = Canvas(window, width=800, height=800)
canvas.pack(fill="both", expand=True)

img1 = PhotoImage(file="box.png")
canvas.create_image(0, 0, image=img1, anchor="nw")

Label(canvas, text="Location:", font=("Helvetica", 15, 'bold'), bg='#f0f0f0').place(x=50, y=44)
location_entry = Entry(canvas)
location_entry.place(x=150, y=50)
Button(canvas, text="Results", command=show_data).place(x=280, y=44)

frame = Frame(canvas, bg='#ffffff', bd=2, relief="groove")
frame.place(x=50, y=100, width=300, height=200)
time_label = Label(frame, text="", font=("Helvetica", 15, "bold"), bg='#ffffff')
time_label.pack(pady=5)
temp_label = Label(frame, text="", font=("Helvetica", 15, "bold"), fg="red", bg='#ffffff')
temp_label.pack(pady=5)
humidity_label = Label(frame, text="", font=("Helvetica", 15, "bold"), fg="blue", bg='#ffffff')
humidity_label.pack(pady=5)
precipitation_label = Label(frame, text="", font=("Helvetica", 15, "bold"), fg="green", bg='#ffffff')
precipitation_label.pack(pady=5)
wind_label = Label(frame, text="", font=("Helvetica", 15, "bold"), fg="purple", bg='#ffffff')
wind_label.pack(pady=5)

img2 = PhotoImage(file="logo.png")
ttk.Label(canvas, image=img2, background='#f0f0f0').place(x=360, y=100)

window.mainloop()
