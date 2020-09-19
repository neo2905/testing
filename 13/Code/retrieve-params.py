import requests
import json
import ast 
import datetime
import time
import csv

t = precip = tmin = tmax = dpoint = humidity = windSpeed = uvIndex = 0
#pressure = pairs['daily']['data'][0]['pressure']


class App(dict):
    def __str__(self):
        return json.dumps(self)


def weather_data(dt,uni):
	res=requests.get('https://api.darksky.net/forecast/**key;)**/19.0760,72.8777,'+uni+'?exclude=currently,flags')
	a = res.json()
	pairs = App(a)
	data_write=[]
	p=pairs['daily']['data'][0]['precipIntensityMax']
	tmi=pairs['daily']['data'][0]['temperatureMin']
	tma=pairs['daily']['data'][0]['temperatureMax']
	d=pairs['daily']['data'][0]['dewPoint']
	h = pairs['daily']['data'][0]['humidity']
	#pressure = pairs['daily']['data'][0]['pressure']
	w=pairs['daily']['data'][0]['windSpeed']
	u= pairs['daily']['data'][0]['uvIndex']
	
	precip = precip + p
	tmin = tmin + tmi
	tmax = tmax + tma
	dpoint = d + dpoint
	windSpeed = windSpeed + w
	humidity = humidity + h
	uvIndex = uvIndex + u
	t = t + 1
	
	if t%7 == 0:
		data_write=[[dt,precip/7,tmin/7,tmax/7,dpoint/7,humidity/7,windSpeed/7,uvIndex/7]]
		print(data_write)
		with open('Parameters.csv','a+') as f:
			write_csv = csv.writer(f)
			write_csv.writerows(data_write)
		precip=tmin=tmax=dpoint=humidity=windSpeed=uvIndex=t=0


def main():
	print()

	for j in range(1,13):
		if j==2:
			for i in range(1,29):
				dt = datetime.datetime(2015,j,i,12,0)
				print(dt)
				dt1=dt.date()
				uni = str(int(time.mktime(dt.timetuple())))
				print(uni)
				weather_data(dt1,uni)

		elif (j==4 or j==6 or j==9 or j==11):
			for i in range(1,31):
				dt = datetime.datetime(2015,j,i,12,0)
				print(dt)
				dt1=dt.date()
				uni = str(int(time.mktime(dt.timetuple())))
				print(uni)
				weather_data(dt1,uni)
		else:
			for i in range(1,32):
				dt = datetime.datetime(2015,j,i,12,0)
				print(dt)
				dt1=dt.date()
				uni = str(int(time.mktime(dt.timetuple())))
				print(uni)
				weather_data(dt1,uni)


if __name__=='__main__':
	main()
  