import requests
from datetime import datetime

def fetch_weather_data(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()
        return weather_data['list']
    except requests.exceptions.RequestException as e:
        print("Error fetching weather data:", str(e))
        return None

def filter_duplicates_by_date(weather_data):
    unique_dates = set()
    filtered_weather_data = []

    for entry in weather_data:
        date = entry['dt_txt'].split(' ')[0]
        if date not in unique_dates:
            filtered_weather_data.append(entry)
            unique_dates.add(date)

    return filtered_weather_data


def format_date(date_string):
    date_obj = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
    formatted_date = date_obj.strftime('%a, %d %b %Y')
    return formatted_date

def main():
    city_name = "Jakarta"  
    api_key = "402085a94477c332acc893ce575e3e3b"  

    weather_data = fetch_weather_data(city_name, api_key)

    if weather_data is not None:
        filtered_weather_data = filter_duplicates_by_date(weather_data)

        print("Weather Forecast:")
        for entry in filtered_weather_data:
            date_time = entry['dt_txt']
            formatted_date = format_date(date_time)
            temperature = entry['main']['temp']
            print(f"{formatted_date}: {temperature}°C")

if __name__ == "__main__":
    main()
