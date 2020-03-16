#!/usr/bin/env python

# Any copyright is dedicated to the Public Domain.
# https://creativecommons.org/publicdomain/zero/1.0/

# Written by Jürgen Kraus <jmk99@me.com>
import matplotlib.pyplot as plt
import numpy as np
import requests
import os, time
import json

def read_data():
	filename = 'corona_lmao_ninja_countries.json'
	delay = 14400 # 4 hours

	if not os.path.isfile(filename) or os.path.getmtime(filename) < time.time() - delay:
		r = requests.get('https://corona.lmao.ninja/countries')
		info = r.json()
		with open(filename, 'w') as fp:
			json.dump(info, fp)
			print('Retrieving new data from source.')
	else:
		t = time.time() - os.path.getmtime(filename)
		next_update = time.strftime('%H:%M:%S', time.gmtime(delay - t))
		with open(filename, 'r') as fp:
			info = json.load(fp)
			print(f'Loading cached data from file. Next update in {next_update}')
	return info

fields = [
	'country', 'cases', 'todayCases', 'deaths', 'todayDeaths', 'recovered',
	'critical'
]

info = read_data()
my_field = fields[1]
info.sort(key=lambda x:x[my_field], reverse=True)
my_info = info[:10]

# Set colors for bars, Germany is always red
my_colors = ['blue'] * len(my_info)
for idx, val in enumerate(my_info):
	if val['country'] == 'Germany':
		my_colors[idx] = 'red'
		break

countries = [x['country'] for x in my_info]
data = [x[my_field] for x in my_info]

y_pos = np.arange(len(countries))
plt.rcdefaults()
ax = plt.subplot(111)
ax.barh(y_pos, data, align='center', alpha=0.5, color=my_colors)
plt.yticks(y_pos, countries)
plt.xlabel(my_field)
plt.title('COVID-19')
for i, v in enumerate(data):
	ax.text(v, i - .15, ' ' + str(v), color='black', fontweight='normal')

plt.show()
