import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('./medical_examination.csv')

# Add 'overweight' column
df['overweight'] = ((df['weight']/(df['height']/100) ** 2) > 25).astype(int)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# Draw Categorical Plot
def draw_cat_plot():
		# Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
		df_cat = pd.melt(df, value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'], id_vars='cardio')

		# Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
		df_cat = df_cat.groupby(['cardio', 'variable'])['value'].value_counts(ascending=True).to_frame('total').reset_index()

		# Draw the catplot with 'sns.catplot()'
		g = sns.catplot(x='variable', y='total', hue='value', col='cardio', kind='bar', data=df_cat)
		fig= g.fig

		# Do not modify the next two lines
		fig.savefig('catplot.png')
		return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
		df_heat = df.loc[(df['ap_lo'] <= df['ap_hi']) & (df.height >= df.height.quantile(.025)) & (df.height <= df.height.quantile(.975)) & (df.weight >= df.weight.quantile(.025)) & (df.weight <= df.weight.quantile(.975))]
		# Calculate the correlation matrix
		corr = df_heat.corr()
		# Generate a mask for the upper triangle
		mask = np.zeros_like(corr)
		mask[np.triu_indices_from(corr)] = True



		# Set up the matplotlib figure
		fig, ax = plt.subplots(figsize=[12.8,10.4])

		# Draw the heatmap with 'sns.heatmap()'
		sns.heatmap(corr, center=0, robust=True, annot=True, fmt='.1f', linewidths=0.5, cbar_kws={'shrink': .45, 'format': '%.2f'}, square=True, xticklabels=True, yticklabels=True, mask=mask)


		# Do not modify the next two lines
		fig.savefig('heatmap.png')
		return fig
