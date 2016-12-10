import numpy as np
import matplotlib.pyplot as plt

def count_missing_values(df):
	"""
	Creates dict of features with count of missing values.
	"""

	columns = df.columns
	missing_val_count = {}

	return {col: df[col].isnull().sum() for col in columns}


def plot_variable_distribution(df, indices, dim):
	fig, ax = plt.subplots(dim, dim, sharey=False, figsize=(15, 15))

	for i, col in enumerate(indices):

		curr_ax  = ax[int(i/dim)][i%dim]
		curr_ax.set_xticklabels(df.columns) # set labels for x-axis
		curr_ax.set_title(df.ix[col].name)  # set title for each of the subplots

		df.ix[col].plot(ax=curr_ax)

		plt.setp(curr_ax.xaxis.get_majorticklabels(), rotation=45)

	plt.tight_layout()


def plot_crosstab_distribution(df):
	num_categories = df.index.nunique()
	categories     = df.index.unique()

	dim = int(np.ceil(num_categories ** 0.5))
	plot_variable_distribution(df, categories, dim)
