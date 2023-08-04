import requests

def get_weather(api_key, city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] == "404":
        print("City not found.")
        return None

    return data

def display_weather(data):
    weather_desc = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    print(f"Weather in {data['name']}: {weather_desc}")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")

if __name__ == "__main__":
    api_key = "f1af04927b9c107d6fa9f221d9f4a716"  # Replace with your OpenWeatherMap API key
    city_name = input("Enter the name of the city: ")

    weather_data = get_weather(api_key, city_name)

    if weather_data:
        display_weather(weather_data)
