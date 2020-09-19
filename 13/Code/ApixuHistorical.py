import requests

api_key = '11bad001e99c4a9b88c74300190409'
api_call = 'https://api.apixu.com/v1/history.json?key='+api_key

city = input('Please input the city name: ')
dt = input('Enter date: ')

date=[]
date = dt.split('-')
dt_count = int(date[2])
dt_count = dt_count - 1
dt_month = int(date[1])
count = 3

while(count != 0):
    if dt_count == 0:
        if (dt_month-1) in [1,3,5,7,8,10,12]:
            dt_count = 31

        elif dt_month - 1 == 2:
            dt_count = 28

        else:
            dt_count = 30
        dt_month = dt_month - 1

    date[1] = dt_month
    count = count - 1
    date[2] = dt_count

    if(date[2] < 10):
        date2 = "0"+str(date[2])
    else:
        date2 = str(date[2])
    
    if(date[1] < 10):
        date1 = "0"+str(date[1])
    else:
        date1 = str(date[1])

    dt = str(date[0])+"-"+date1+"-"+date2

    pressure_count=0
    pressure=0
    api_key = '11bad001e99c4a9b88c74300190409'
    api_call = 'https://api.apixu.com/v1/history.json?key='+api_key
    api_call += '&q='+city+'&dt='+dt
    json_data = requests.get(api_call).json()
    temp_min = json_data['forecast']['forecastday'][0]['day']['mintemp_c']
    temp_max = json_data['forecast']['forecastday'][0]['day']['maxtemp_c']
    wind_speed = json_data['forecast']['forecastday'][0]['day']['maxwind_kph']
    prept = json_data['forecast']['forecastday'][0]['day']['totalprecip_mm']
    humidity = json_data['forecast']['forecastday'][0]['day']['avghumidity']
    
    while(pressure_count<24):
        pressure += json_data['forecast']['forecastday'][0]['hour'][pressure_count]['pressure_mb']
        pressure_count+=1

    pressure /= 24
    wind_speed *= 5/18

    print("Date: "+dt)
    print("Min temp  : {}°C".format(temp_min))
    print("Max temp  : {}°C".format(temp_max))
    print("Wind speed: {0:.2f} m/s".format(wind_speed))
    print("Pressure: {0:.2f} hpa".format(pressure))
    print("Humidity  : {} %".format(humidity))
    print("Precipitation: {} mm".format(prept))
    print("\n")

    dt_count -= 1


























