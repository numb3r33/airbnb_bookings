import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy as sp

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

def create_days_since_creation_mapping(days_since_creation):
	if pd.isnull(days_since_creation):
		return -9999 # represents missing value
	elif days_since_creation == 0:
		return 0
	elif days_since_creation > 0 and days_since_creation <= 365:
		return 1
	elif days_since_creation < 0 and days_since_creation >= -365:
		return 2

def chi_square_test(X, y):
	"""

	Note: (the smaller v, the lower the correlation)

	Arguments
	---------

	X - single feature
	y - target

	Returns
	-------

	p_val    : P-value
	cramer_v : Cramer-V value
	"""

	cont_table = pd.crosstab(X, y)
	chi2_statistic, p_val, dof, expected = sp.stats.chi2_contingency(cont_table.values, correction=False)
	print('P-value for the pair : %f'%(p_val))


	cramer_v = np.sqrt(chi2_statistic / (len(cont_table) * min(cont_table.shape[0], cont_table.shape[1])))
	print('Cramer-V value for pair : %f'%(cramer_v))

	return p_val, cramer_v
