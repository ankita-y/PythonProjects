import requests, json

api_key = "cbe73866ef595119022bfdaec1fb8466"

base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter City Name: ")
complete_url = base_url + "q="+ city_name + "&appid=" + api_key

response = requests.get(complete_url)
x = response.json()

try:
    if x["cod"] != "404":
        y = x["main"]
        temp = y["temp"]
        temp = round(temp - 273.15,2)
        pressure = y["pressure"]
        humidity = y["humidity"]
        z = x["weather"]
        description = z[0]["description"]

        print("="*20)
        print("City: " + city_name)
        print("Temperature: " + str(temp)+"ºC")
        print("Pressure: " + str(pressure) + "hpa")
        print("Humidity: " + str(humidity) + "%")
        print("Day: " + description)
        print("=" * 20)
    else:
        print("City Not Found")



except Exception as e:
    print("Invalid API Key" + e)




