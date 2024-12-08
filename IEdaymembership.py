#import packages
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# #location of the file with your dat
filedir = <<put your route here>>>

#loading data
data = pd.read_csv(filedir + r'\Membership_1724_raw.csv')
data.head()
#anonymize the column member by substituting names with aleatory codes, keepiong the same code for the same member
data['Member'] = data['Member'].astype('category')
data['Member'] = data['Member'].cat.codes
data.head()

# create new field 'fortnight' to group days between 1 and 15 as '1' and 16 to 31 as '2', then the number of the month
data['Date'] = pd.to_datetime(data['Date'])
data['Month'] = data['Date'].dt.month
data['Month'] = data['Month'].astype('category')
data ['Year'] = data['Date'].dt.year
data['Day'] = data['Date'].dt.day
data['DayMonth'] = data['Day'].astype(str) + '-' + data['Month'].astype(str)
data['DayMonth'] = pd.to_datetime(data['DayMonth'], format='%d-%m')


data.head()


#plot the number of renewals by fortnight and year
sns.set_theme(style="whitegrid")
g= sns.displot(data, x='Month', hue='Type', multiple='stack',
                 col='Year', col_wrap =3, facet_kws=dict(margin_titles=True) ,
                 height=4, aspect=1, kind='hist', label='big')

g.set_axis_labels("Month", "Payment registrations")
g.set_titles("{col_name}")
plt.show()
#save the plot
g.savefig(filedir + r'\Membership_1724.png')

#
#plot new members in year 2024 by day showing all days
sns.set_theme(style="white")
g = sns.displot(data, x='DayMonth', hue='Type', multiple='stack',
                col='Year',col_wrap=2,
                height=4, aspect=2,
                kind='hist',  binwidth=1, legend=True)

# Adjust the legend position to the bottom
g.fig.subplots_adjust(left=0.1, bottom=0.15, right=0.80)  # Adjust the bottom margin to make space for the legend

#format of labels
for ax in g.axes.flat:
    ticks = pd.date_range(start=data['DayMonth'].min(), end=data['DayMonth'].max(), freq='15D')
    ax.set_xticks(ticks)
    ax.set_xticklabels([tick.strftime('%d-%m') for tick in ticks], rotation=90, fontsize=16)
    ax.yaxis.grid(True)
    ax.set_yticklabels(ax.get_yticks(), fontsize=16)
    ax.axvline(pd.to_datetime('1-11', format='%d-%m'), color='lightgrey', linestyle='--')
    ax.axvline(pd.to_datetime('30-11', format='%d-%m'), color='lightgrey', linestyle='--')

#set titles etc
g.set_axis_labels("\nDay of the year", "Payment registrations\n", fontsize=20)
g.set_titles("{col_name}", size=20)
g.legend.set_title('Types', prop={'size': 20})
for text in g.legend.get_texts():
    text.set_fontsize(16)
plt.show()
#save the plot
g.savefig(filedir + r'\Membership_1924_day.png', dpi=500)


