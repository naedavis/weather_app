from tkinter import messagebox

import requests
import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry("500x500")
root.config(bg="teal")
root.title("Current Weather")

e_search = Entry(root, font="Arial 20", fg="teal")
e_search.place(x=100,y=40, width =200, height= 50)
btn_search = Button(root, text="Search City", font="Arial 15", bg="yellow")
btn_search.place(x=320,y=40, height=50)

lbl_city =Label(root,text="Cape Town", fg="white", bg="teal", font="Arial 20")
lbl_city.place(x=150, y= 110)
lbl_current_temp = Label(root, text="28", fg="white", bg="teal", font="Arial 50")
lbl_current_temp.place(x=180, y=150)
lbl_cloudiness = Label(root, text="0%", fg="white", bg="teal", font="Arial 20")
lbl_cloudiness.place(x=200, y=230)
lbl_min = Label(root, fg="white", bg="teal", font="Arial 15")
# lbl_min.place(x=)




url = 'http://api.openweathermap.org/data/2.5/weather?'
key = '4b9599c6b999d259bb64a21f9d571a24'
parameters = {'q': 'Cape Town', 'appid':key, 'units':'metric'}

response = requests.get(url, params=parameters)
data = response.json()
# print( "Max temperature is "+ str(data['main']['temp_max']))
print(data['main'])
# print(data['clouds']['all'])
root.mainloop()