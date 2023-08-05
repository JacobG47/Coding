import json

import requests

base_url = "https://api.openweathermap.org/data/2.5/weather"
appid = "7592f7acba3d98cc0d44bd0bee588846"

def get_weather_data(location):
  try:
   
  # isdigit method checks if the input is text and the len function checks if it is 5 digits
    
     if location.isdigit() and len(location) == 5:
      url = f"{base_url}?zip={location}&units=imperial&APPID={appid}"
              
     else:
      url = f"{base_url}?q={location}&units=imperial&APPID={appid}"

     response = requests.get(url)
# status code 200 means that the connection to the internet server was succesful
     if response.status_code == 200:
         try:
              return response.json()
         except ValueError:
           print("Invalid response from the weather site. Please try again.")
           return None
     else:
       print("Invalid zip or city. Please try again.")

  except requests.exceptions.RequestException:
    print("Having trouble connecting to the service...")
    return None

def display_weather_forecast(weather_data):
  
    if weather_data:
      
        city = weather_data.get("name", "Unknown City")
        country = weather_data.get("sys", {}).get("country", "Unknown Country")
        temp = weather_data.get("main", {}).get("temp", "Unknown")
        

        print(f"Weather forecast for {city}, {country}:")
        print(f"Temperature: {temp} °F")
    else:
        print("Weather data not available for the given location.")

def main():
    while True:
        location = input("Please enter a zip code or city name (or '0' to quit): ")
      # if user enters '0' it quits the program and sends a thank you message
        if location == '0':
         break
         
        weather_data = get_weather_data(location)
      
        if weather_data:
          display_weather_forecast(weather_data)

    print('Thank you for using my weather machine!')



if __name__ == "__main__":
    main()

