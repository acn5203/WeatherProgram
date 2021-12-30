import requests
import datetime

x = ""


def get_weather(city):

	api_key = "85d0179d80e47a439325d88fc8ea768b"

	api_url = "https://api.openweathermap.org/data/2.5/weather"

	params = {"APPID": api_key, "q": city, "units": "imperial"}

	response = requests.get(api_url, params=params)

	weather = response.json()


	try:

		climate = weather["weather"][0]["main"]

		temp = weather["main"]["temp"]

		name = weather["name"]


		print("Name:", name)

		print("Weather: ", climate)

		print("Temperature (Farenheight):", temp)

		print("........")

	except:

		print("There was an error computing")

		print("......")

        

while x != "QUIT":


        today = datetime.date.today()

        time = datetime.datetime.now()

        y = today.strftime("%b %d")

        z = time.strftime("%H:%M")

        print("To exit, type QUIT")

        print("Date:", y, "Time:", z)

        x = input("Please enter the name of a city or zipcode: ")

        if x == "QUIT":
                exit()
        else:
                get_weather(x)



