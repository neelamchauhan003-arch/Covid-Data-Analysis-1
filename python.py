import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns} 
import warnings
warnings.filterwarnings("ignore")

df= pd.read_csv('country_wise_latest.csv')
df
df.head(10)
df.shape
df.columns
df.info()
df.describe()
df['Deaths / 100 Cases'] = df['Deaths / 100 Cases']. astype('int')
df['Recovered / 100 Cases'] = df['Recovered / 100 Cases']. astype('int')
df.info()
df.head(10)
plt.figure(figsize=(15,6))
ax = sns.countplot(data=df.head(10),x ='Active', hue = 'Country/Region') # Plotting counts of Country/Region
plt.title('Active CASES by Country/Region')
for bars in ax.containers:
    ax.bar_label(bars) # Add labels to the bars
plt.show()
top_region = df.groupby('Country/Region')[['Confirmed', 'Deaths', 'Recovered','Active']].sum()
top_region = top_region.sort_values('Confirmed', ascending=False).head(10)

top_region.plot(kind='barh', title='Top 10 Countries - Covid Cases')
plt.show()
df.columns

cases_region = df.groupby('WHO Region')[['Active']].sum().head(20)

cases_region['Active'].plot(
    kind='pie',
    subplots = True,
    autopct='%1.2f%%',
    ylabel='',
    title='Active Cases by WHO Region'
)
plt.show()

cases_region = df.groupby('WHO Region')[['New cases', 'New deaths', 'New recovered']].sum()

# Create subplots (3 pie charts in a row)
fig, axes = plt.subplots(1, 3, figsize=(18,6))

for i, column in enumerate(cases_region.columns):
    cases_region[column].plot(
        kind='pie',
        autopct='%1.2f%%',
        ax=axes[i],
        ylabel='',   # removes default y-label
        title=column + " by WHO Region"
    )

plt.show()

monthly = df.groupby('Country/Region')[['Confirmed last week','1 week change','1 week % increase']].sum().head(15) #double brackets- select muliple columns in a list
monthly.plot(kind='line',figsize=(12,6),title= 'week analysis') #dont chained head after plot
plt.show()
monthly = df.groupby('Country/Region')[['Deaths / 100 Cases','Recovered / 100 Cases','Deaths / 100 Recovered']].sum().head(15) #double brackets- select muliple columns in a list
monthly.plot(kind='bar',figsize=(12,6),title= 'Covid Cases analysis') #dont chained head after plot
plt.show()

# Histogram for deaths per 100 cases
sns.histplot(data=df, x='Deaths / 100 Cases', bins=50, kde=True)
plt.title('Distribution of Deaths / 100 Cases')
plt.show()

# Histogram for recovered per 100 cases
sns.histplot(data=df, x='Recovered / 100 Cases', bins=50, kde=True)
plt.title('Distribution of Recovered per 100 Cases')
plt.show()

# Histogram for deaths per 100 recovered
sns.histplot(data=df, x='Deaths / 100 Recovered', bins=50, kde=True)
plt.title('Distribution of Deaths / 100 Recovered')
plt.show()

monthly = df.groupby('Country/Region')[['Recovered','New recovered','Recovered / 100 Cases']].sum().head(15) #double brackets- select muliple columns in a list
monthly.plot(kind='bar',figsize=(12,6),title= 'Recovered Covid Cases analysis') #dont chained head after plot
plt.show()

cases_region = df.groupby('Country/Region')[['Recovered', 'New recovered', 'Recovered / 100 Cases']].sum().head(10)

# Create subplots (3 in a row)
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Loop through columns and axes together
for ax, column in zip(axes, cases_region.columns):
    cases_region[column].plot(
        kind='bar',
        ax=ax,   # 👈 tell it which subplot to use
        ylabel='', 
        title=column + " by Country/Region"
    )

plt.tight_layout()
plt.show()

monthly = df.groupby('Country/Region')[['Confirmed','New cases','Active']].sum().head(15) #double brackets- select muliple columns in a list
monthly.plot(kind='bar',figsize=(12,6),title= ' Covid Cases analysis') #dont chained head after plot
plt.show()

cases_region = df.groupby('Country/Region')[['Confirmed', 'New cases', 'Active']].sum().head(10)

# Create subplots (3 in a row)
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Loop through columns and axes together
for ax, column in zip(axes, cases_region.columns):
    cases_region[column].plot(
        kind='bar',
        ax=ax,   # 👈 tell it which subplot to use
        ylabel='', 
        title=column + " by Country/Region"
    )

plt.tight_layout()
plt.show()

plt.figure(figsize=(12,6))
sns.scatterplot(data=df.head(10),x ='Country/Region', y='Confirmed last week',hue='Confirmed last week',sizes=(100, 500))
plt.title("Confirmed last week(Active)", fontsize=14,color='green')
plt.xlabel("Country/Region",color='green')
plt.ylabel("Confirmed last week",color='blue')
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(15,6))
sns.boxplot(data=df.head(10),x ='Country/Region',y='Active',hue  ='Active')
plt.title('Rating Data')
