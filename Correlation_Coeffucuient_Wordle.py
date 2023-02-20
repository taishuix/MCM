import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl
import numpy as np

data1 = pd.read_excel("task2(5).xlsx", engine='openpyxl')
df1 = pd.DataFrame(data1)
df1.pop('date')
df1.pop('log_word_fre')
df1.pop('word_fre')
df1.pop('10000inv_word_fre')
df1.pop('score')


df_coor = df1.corr('spearman')
df_coor.head()

mask = np.zeros_like(df_coor)
mask = mask[11:, :-4]
corr = df_coor.iloc[11:, :-4].copy()


f, ax = plt.subplots(figsize=(9, 9), dpi=300, facecolor='w')
fig = sns.heatmap(corr, annot=True, vmax=1,vmin=-1, square=True, cmap='coolwarm', cbar_kws={'orientation': 'horizontal', "pad":0.2}, linewidths=0.05,fmt='.2f',annot_kws={'size': 6})
label_x = ax.get_xticklabels()
plt.setp(label_x, rotation=30, horizontalalignment='right')
fig.tick_params(labelsize=5)
cax = plt.gcf().axes[-1]
cax.tick_params(labelsize=5)
fig.get_figure().savefig('df_corr_Wordle_spearman.png', bbox_inches='tight', transparent=True)
plt.show()

plt.cla()