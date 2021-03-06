#!/usr/bin/env python

# Any copyright is dedicated to the Public Domain.
# https://creativecommons.org/publicdomain/zero/1.0/

# Written by Jürgen Kraus <jmk99@me.com>
import matplotlib.pyplot as plt
import numpy as np
import requests
import os, time
import json
import sys


def debug_data(payload, field):
	for entry in payload:
		print(f"{entry['country']}: {entry[field]}")
	sys.exit()


def read_data(force=False):
	filename = 'corona_lmao_ninja_countries.json'
	delay = 14400  # 4 hours

	if force is True or not os.path.isfile(
			filename) or os.path.getmtime(filename) < time.time() - delay:
		r = requests.get('https://corona.lmao.ninja/v2/countries')
		info = r.json()
		with open(filename, 'w') as fp:
			json.dump(info, fp)
			print('Retrieving new data from source.')
	else:
		t = time.time() - os.path.getmtime(filename)
		next_update = format_time(delay - t)
		with open(filename, 'r') as fp:
			info = json.load(fp)
			print(f'Loading data from cache. Next cache update in {next_update}')
	return info


def format_time(value):
	return time.strftime('%H:%M:%S', time.gmtime(value))


def format_date(value):
	return time.strftime('%c', time.gmtime(value / 1000))


def format_value(number):
	val = '{:,}'.format(number)
	return val.replace(',', '.')


def get_single_country(info, country):
	for record in info:
		if record['country'] == country:
			return record


fields = [
	'country', 'cases', 'todayCases', 'deaths', 'todayDeaths', 'recovered',
	'critical'
]

info = read_data()
my_country = 'Germany'
my_country_record = get_single_country(info, my_country)
last_update = my_country_record['updated']
print(f'Last data update ({my_country}): ' + format_date(last_update))

for i in (1, 2, 3, 4):
	# Reset Diagram
	plt.clf()
	#configuration
	my_field = fields[i]
	#debug_data(info, my_field)

	# Compile data from source
	info.sort(key=lambda x: x[my_field], reverse=True)
	my_info = info[:10]
	
	# Check if my_country is part of the top 10
	my_country_top10 = False
	for record in my_info:
		if record['country'] == my_country:
			my_country_top10 = True
			break
	if my_country_top10 is False:
		my_info.insert(10, my_country_record)

	# Set colors for bars and rank number, my_country is always red
	my_colors = ['blue'] * len(my_info)
	for idx, val in enumerate(my_info):
		if val['country'] == my_country:
			my_colors[idx] = 'red'
			break

	countries = [x['country'] for x in my_info]
	data = [x[my_field] for x in my_info]

	y_pos = np.arange(len(countries))
	ax = plt.subplot(111)
	ax.barh(y_pos, data, height=0.8, align='center', alpha=0.5, color=my_colors)
	plt.yticks(y_pos, countries)
	plt.xlabel(my_field)
	plt.title('COVID-19')
	for i, v in enumerate(data):
		ax.text(
			v,
			i - .15,
			' ' + format_value(v),
			size='9',
			color='#555555',
			fontweight='normal')

	plt.show()

