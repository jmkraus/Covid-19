import requests

#Put your own country here:
country = 'Germany'

r = requests.get('https://corona.lmao.ninja/countries')
info = r.json()
my_info = [c for c in info if c['country'] == country]
if my_info:
	print(f'Cases today in {country}: {my_info[0]["todayCases"]}')
else:
	print(f'No data for this country: {country}')
