from django.shortcuts import render
import requests

def weather_data(request):
	if request.method == 'POST':
		city = request.POST['city'].strip()
		# source contain JSON data from API

		source = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=789bbc0334b3a29852a81327c810f5fc')
		if source.status_code != 200:
			return render(request, "weather/index.html", {"msg":"Something went wrong"})

		# converting JSON data to a dictionary
		list_of_data = source.json()

		# data for variable list_of_data
		data = {"weather_data":
			{
				"country_code": str(list_of_data['sys']['country']),
				"coordinate": str(list_of_data['coord']['lon']) + ' '+ str(list_of_data['coord']['lat']),
				"temp": str(list_of_data['main']['temp']) + 'k',
				"pressure": str(list_of_data['main']['pressure']),
				"humidity": str(list_of_data['main']['humidity']),
			}
		}
	else:
		data ={}
	return render(request, "weather/index.html", data)
