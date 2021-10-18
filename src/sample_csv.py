import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/robomech_anstime.csv', sep=',')
df.columns = ['cond', 'sec']

ax = sns.swarmplot(x='cond', y='sec', data=df, size=10)
# ax = sns.swarmplot(x='cond', y='sec', data=df, size=10, hue='match', dodge=True, palette='Set2')
ax = sns.boxplot(x='cond',
                 y='sec',
                 data=df,
                #  hue='match',
                 showmeans=True,
                 meanline=True,
                 meanprops={'color': 'k', 'ls': '-', 'lw': 2},
                 medianprops={'visible': False},
                 whiskerprops={'visible': False},
                 zorder=10,
                 showfliers=False,
                 showbox=False,
                 showcaps=False,
                 ax=ax)

# hueを使うときに凡例を調整するための処理
# handles, labels = ax.get_legend_handles_labels()
# l = plt.legend(handles[2:4], labels[2:4], loc=2)

plt.show()
