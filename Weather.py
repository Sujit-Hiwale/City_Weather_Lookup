import requests
try:
	api_key = '9717adbddc9a9bdca3ae1c7299d51ca0'
	city = input("Enter your city: ")
	data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?&q={city}&units=imperial&APPID={api_key}")
	if data.json()['cod'] == '404':
		print("City not found.")
	else:
		weather = data.json()['weather'][0]['main']
		temp_f = round(data.json()['main']['temp'])
		temp_c = round(5/9*(temp_f-32))
		humidity = data.json()['main']['humidity']
		pressure = data.json()['main']['pressure']
		print('Weather: ' + weather)
		print('Temperature: ' + str(temp_c) + '°C (' + str(temp_f) + "°F)")
		print('Humidity: ' + str(humidity) + '%')
		print('Pressure: ' + str(pressure) + 'mbar')
except requests.exceptions.RequestException as e:
	print(f'An error occured:')
	print('There seems to be an issue with your connection.')
	print('Please check your network connection and try again.')