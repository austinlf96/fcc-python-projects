import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
	# Read data from file
	df = pd.read_csv('epa-sea-level.csv')
	x = df['Year']
	y = df['CSIRO Adjusted Sea Level']

	# Create scatter plot
	fig, ax = plt.subplots(figsize=[9.8, 7.2])
	plt.scatter(x, y, s=10.0)

	# Create first line of best fit
	slope, intercept, r_value, p_value, std_err = linregress(x, y)
	x = range(x[0], 2050)
	plt.plot(x, intercept + slope*x, '-r', data=df)

	# Create second line of best fit
	df2 = df[df['Year'] > 1999]
	x2 = df2['Year']
	y2 = df2['CSIRO Adjusted Sea Level']
	slope2, intercept2, r_value2, p_value2, std_err2 = linregress(x2, y2)
	x2 = range(df2.iat[0,0], 2050)
	plt.plot(x2, intercept2 + slope2*x2, '-g')

	# Add labels and title
	ax.set_title('Rise in Sea Level')
	ax.set_xlabel('Year')
	ax.set_ylabel('Sea Level (inches)')

	# Save plot and return data for testing (DO NOT MODIFY)
	plt.savefig('sea_level_plot.png')
	return plt.gca()