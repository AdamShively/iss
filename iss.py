import requests
import webbrowser
import turtle
import tkinter as tk

class Iss:
    
    def __init__(self):
        self.window = turtle.Screen()
        self.astro_text = turtle.Turtle()
        self.not_displayed = True

    #Displays or clears astronaut info.
    def show_astros(self):
        self.astro_text.hideturtle()
        if self.not_displayed:
            self.astro_text.color("black")
            self.astro_text.penup()
            self.astro_text.goto(0, -50)
            self.astro_text.write(Iss.astroInfo(), align="center", font=("Helvetica Narrow", 20 , "bold"))

        else:
            self.astro_text.clear()

        self.not_displayed = not self.not_displayed

    #Get number of astronaut, names of astronauts and associated craft to add to string.
    def astroInfo():
        url = "http://api.open-notify.org/astros.json"  #Request info from API
        response = requests.get(url)
        res = response.json()
        result = f"There are {res['number']} astronauts in space:\n"
        people = res['people']
        for person in people:
            result += f"Astronaut: {person['name']}, Craft: {person['craft']} \n"
        return result

    #Open link in a browser.
    def facts_figures(self):
        webbrowser.open("https://www.nasa.gov/feature/facts-and-figures") 

    #Open link in a browser.
    def nasa_tv(self):
        webbrowser.open("https://www.nasa.gov/multimedia/nasatv/index.html?channel=iss#media") 

    #Create window with world map picture
    def create_window(self):
        self.window.setup(1419, 720)
        self.window.bgpic("map.gif")
        self.window.setworldcoordinates(-180, -90, 180, 90)
        self.window.title("International Space Station")
        self.window.tracer(0)
        
        self.window.register_shape("iss.gif")
        self.window.screensize()
        self.window.setup(width = 1.0, height = 1.0)
        self.window.setup(width=1.0, height=1.0)

    #Creates option buttons for window.
    def create_buttons(self):
        canvas = self.window.getcanvas()

        #Button for astronaut info
        astro_button = tk.Button(canvas.master, text="Toggle Astronaut Info", command=self.show_astros)
        canvas.create_window(620, -310, window=astro_button)

        #Button for ISS Facts and Figures
        ff_button = tk.Button(canvas.master, text="ISS Facts and Figures", command= self.facts_figures)
        canvas.create_window((620,310), window=ff_button)

        #Button for ISS Video Coverage
        website_button = tk.Button(canvas.master, text="ISS Video Coverage", command=self.nasa_tv)
        canvas.create_window((-620,310), window=website_button)

def main():
    iss = Iss()
    iss.create_window()
    iss.create_buttons()
    iss.astro_text.hideturtle()

    #Create ISS representation
    ship = turtle.Turtle()  
    ship.shape("iss.gif")
    ship.setheading(45)
    ship.penup()

    #Create Turtle object for ISS current latitude and longitude info
    ll_text = turtle.Turtle()
    ll_text.hideturtle()

    while True:

        #Request info from API
        url = "http://api.open-notify.org/iss-now.json"
        response = requests.get(url)
        res = response.json()

        #Get ISS latitude and longitude
        position = res["iss_position"]
        latitude = position['latitude']
        longitude = position['longitude']

        ship.goto(float(longitude), float(latitude))

        #Clear previous latitude and longitude and display updated
        latlong = f"Postion of ISS\nLatitude: {latitude} \nLongitude: {longitude}"
        ll_text.clear()
        ll_text.penup()
        ll_text.goto(-160, 75)
        ll_text.write(latlong, align="center", font=("Helvetica Narrow", 12 , "bold"))
        iss.window.update()

if __name__ == "__main__":
    main()
