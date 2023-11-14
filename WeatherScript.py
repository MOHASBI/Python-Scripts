import requests

API_KEY="710e5c3e91a4edcf46002f066fa50ca4"
BASE_URL="https://api.openweathermap.org/data/2.5/weather"

city=input("Please input a city name: ")
request_url=f"{BASE_URL}?appid={API_KEY}&q={city}"
response=requests.get(request_url)

if response.status_code==200:
    data=response.json()
    weather=data['weather'][0]['description']
    print(weather)
    temperature=data["main"]["temp"]-273.15
    print(temperature)
else:
    print("An error occured.")