import tkinter as tk
from PIL import Image, ImageTk
import requests
from tkinter import font

height = 500
width = 600

# def test_function(entry):
#     print("This is your entry: ", entry)

# #f589ef488adadc9a6e7abae440787cf9
# api.openweathermap.org/data/2.5/forecast?q={city name}&appid={your api key}
# api.openweathermap.org/data/2.5/forecast?q={city name},{state code}&appid={your api key}
# api.openweathermap.org/data/2.5/forecast?q={city name},{state code},{country code}&appid={your api key}

def format_response(weather):
    
    try:
        name = weather['name']
        description = weather['weather'][0]['description']
        temp = weather['main']['temp']
        
        final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (name, description, temp)
        
    except:
        final_str = 'There was an issue retrieving \nthat information.'

    return final_str
    #return str(name) + " " + str(description) + " " + str(temp)

def get_weather(city):
    weather_key = 'f589ef488adadc9a6e7abae440787cf9'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q':city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()

    #places our weather indicators into our big label box
    label['text'] = format_response(weather)


root = tk.Tk()
#all widgets go in here

canvas = tk.Canvas(root, height=height, width=width)
canvas.pack()

#background_image = tk.PhotoImage(file='animeweather.png')
background_image = ImageTk.PhotoImage(Image.open('grass.jpg'))
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Courier',10), justify = 'center')
#entry.pack(side='left', fill='both')
#entry.grid(row=0, column=2) 
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text = "Get Weather", bg = 'gray', fg = 'black', font=('Courier',10), 
command=lambda: get_weather(entry.get()))
#button.pack(side='left', fill='both', expand=True)
#button.grid(row=0, column=0)
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier',13))
#label.pack(side='left', fill='both')
#label.grid(row=0, column=1)
label.place(relwidth=1, relheight=1)
#print(tk.font.families())

root.mainloop()
