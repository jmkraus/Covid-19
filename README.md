# Covid-19

A collection of small scripts to fetch statistical data on Covid-19 cases for noodling around. All of these scripts work with [Pythonista](https://itunes.apple.com/us/app/pythonista-3/id1085978097?ls=1&mt=8) on Apple iPads. So please bear in mind: there might be better solutions with other libraries, but not all of them are available on Pythonista.

## Corona.py

This is a nice script written by Francois Fleuret. Brought to attention by Ole Zorn on Twitter. Link to original file: <http://fleuret.org/git-extract/python/covid19.py>

Oh, and thanks to Francois for the great idea of "gentle download"! :)

## Covid19-1.py

Sample script by Ole Zorn (Developer of Pythonista) released on Twitter: <https://twitter.com/olemoritz/status/1238660638978736128>

## Covid19-2.py

My somewhat "extended" version of the Ole Zorn script. It takes the sorted top 10 of each field and creates a diagram.

Edit line `my_field = fields[1]` to another field index for different data.

| index | field       |
| ----- | ----------- |
| 1     | cases       |
| 2     | todayCases  |
| 3     | deaths      |
| 4     | todayDeaths |
| 5     | recovered   |
| 6     | critical    |

Set line `world = False` to True if you want a diagram bar with a world total.

**Stay healthy and take care of yourself!**
