import requests
import streamlit as st

# OpenWeatherMap API key
api_key = "a6f81aff8e354cf14db2c448cbb27e5c"

def weather(city):
    """Fetch weather data from OpenWeatherMap API."""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

def main():
    st.title("Weather App")

    city = st.text_input("Enter city name")

    if city:
        if st.button("submit"):
            data = weather(city)

            if data.get("cod") == 200:
                st.subheader(f"Weather in {data['name']}, {data['sys']['country']}")
                st.write(f"Temperature: {data['main']['temp']}°C")
                st.write(f"Humidity: {data['main']['humidity']}%")
                st.write(f"Weather: {data['weather'][0]['description'].capitalize()}")
                st.write(f"Wind Speed: {data['wind']['speed']} m/s")
            else:
                st.error("City not found. Please check the name and try again.")

if __name__ == "__main__":
    main()
