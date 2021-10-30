import requests


# urlOne='https://api.covid19india.org/data.json'
# covidData=requests.get(urlOne).json()

# # data=covidData['statewise']['state']
# # print(data)
# mystate='maharashtra'
# for d in covidData['statewise']:
#     if d['state']==mystate.title():
#         print(d['active'])



loc='Pune'
 
url='http://api.openweathermap.org/data/2.5/weather?q={}&appid=yourKey'.format(loc)
data=requests.get(url).json()
print(data)


data_weather_clouds=data['weather'][0]['description']
print(data_weather_clouds)