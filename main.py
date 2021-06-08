# Naeemah Davis
# Weather App
# an app that will return the weather of any given city
from tkinter import messagebox

import requests
import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry("500x500")
root.config(bg="teal")
root.title("Current Weather")
root.resizable(width="false", height="false")
e_search = Entry(root, font="Arial 20", fg="teal")
#seeting focus to the entry so that the user can immediately enter intsead of selecting the entry first and then entering a city
e_search.focus_set()
e_search.place(x=100, y=40, width=200, height=50)

#functionality for when the search button is clicked
def weather():
    try:
    #VARIABLES
        # #declaring a variable that will hold my url fo rmy weather API
        url = 'http://api.openweathermap.org/data/2.5/weather?'
        # #variable for my api key given
        key = '4b9599c6b999d259bb64a21f9d571a24'
        # variable that will get the input from the user
        city = e_search.get()
        # built in parameters from the api to get the values in a dictionary
        parameters = {'q': city, 'appid': key, 'units': 'metric'}
        response = requests.get(url, params=parameters)
        data = response.json()

        #having a variable to store the current temp that was fetched from the weather API
        current_temp = str(round(data['main']['temp'])) + " °C"
        cloudiness = str(data['clouds']['all']) + " %"
        min_temp = str(round(data['main']['temp_min'])) + " °C"
        max_temp = str(round(data['main']['temp_max'])) + " °C"
        pressure = str(data['main']['pressure']) + " hPa"
        humidity = str(data['main']['humidity']) + " %"
        wind = str(data['wind']['speed']) + " m/s"
        description = data['weather'][0]['description']
        # actions
    # changing the text of each label to a variable declared and that holds the information that was taken from the weather API
        lbl_city.config(text=city)
        lbl_current_temp.config(text=current_temp)
        lbl_cloudiness2.config(text=cloudiness)
        lbl_min2.config(text=min_temp)
        lbl_max2.config(text=max_temp)
        lbl_pressure2.config(text=pressure)
        lbl_humidity2.config(text=humidity)
        lbl_wind2.config(text=wind)
        lbl_description.config(text=description)
    #except KeyError to prevent an invalid input in the City Entry
    except KeyError:
        messagebox.showerror("Error", "Invalid City input")
        e_search.delete(0, END)
    #except that prevents the user from getting an error in case there is no internet connection
    except requests.exceptions.ConnectionError as x:
        messagebox.showerror(" Connection Error", "Please Connect to internet")

#button that will call the function defined above to be executed
btn_search = Button(root, text="Search City", font="Arial 15", bg="yellow", command=weather)
btn_search.place(x=320, y=40, height=50)

lbl_city = Label(root, text="City", fg="white", bg="teal", font="Arial 20")
lbl_city.place(x=150, y=110)

lbl_current_temp = Label(root, text="°C", fg="white", bg="teal", font="Arial 50")
lbl_current_temp.place(x=180, y=150)

lbl_description = Label(root, text="Partly Cloudy", fg="white", bg="teal", font="Arial 16")
lbl_description.place(x=170, y=237)

lbl_cloudiness = Label(root, text="Cloudiness:", fg="white", bg="teal", font="Arial 12")
lbl_cloudiness.place(x=270, y=360)
lbl_cloudiness2 = Label(root, fg="white", bg="teal", font="Arial 12 bold")
lbl_cloudiness2.place(x=390, y=360)

lbl_min = Label(root, text="Min Temp(°C):", fg="white", bg="teal", font="Arial 12")
lbl_min.place(x=80, y=280)
lbl_min2 = Label(root, fg="white", bg="teal", font="Arial 12 bold")
lbl_min2.place(x=190, y=280)

lbl_max = Label(root, text="Max Temp(°C):", fg="white", bg="teal", font="Arial 12")
lbl_max.place(x=270, y=280)
lbl_max2 = Label(root, fg="white", bg="teal", font="Arial 12 bold")
lbl_max2.place(x=390, y=280)

lbl_pressure = Label(root, text="Pressure:", fg="white", bg="teal", font="Arial 12")
lbl_pressure.place(x=80, y=320)
lbl_pressure2 = Label(root, fg="white", bg="teal", font="Arial 12 bold")
lbl_pressure2.place(x=190, y=320)

lbl_humidity = Label(root, text="Humidity:", fg="white", bg="teal", font="Arial 12")
lbl_humidity.place(x=270, y=320)
lbl_humidity2 = Label(root, fg="white", bg="teal", font="Arial 12 bold")
lbl_humidity2.place(x=390, y=320)

lbl_wind = Label(root, text="Wind:", fg="white", bg="teal", font="Arial 12")
lbl_wind.place(x=80, y=360)
lbl_wind2 = Label(root, fg="white", bg="teal", font="Arial 12 bold")
lbl_wind2.place(x=190, y=360)

lbl_made = Label(root, text="Made by Naeemah Davis", fg="white", bg="teal", font="Arial 7 bold")
lbl_made.place(x=350, y=475)

root.mainloop()
