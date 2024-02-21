import json

def find_weather_data(id):
    with open('weather.json') as f:
        data = json.load(f)
        
        for forecast_list in data.values():
            for forecast in forecast_list:
                if forecast['id'] == id:
                    print(f"log: {forecast['log']}")
                    return forecast['status']

def get_status_from_id(id):
    status = find_weather_data(id)
    if status:
        return status
    else:
        return None