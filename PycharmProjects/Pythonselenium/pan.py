import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import quandl
import html5lib


#s = pd.Series({'a':0, 'b':1, 'c': 9})

'''
saleVolume = [100, 200, 300]
year = [2016, 2017, 2018]
s = pd.Series(saleVolume, index=year)

print(s[year[0]])
s.plot()
#Series ([4,5,7]).plot()
plt.show()

dfindex = [1,2,3,4,5]
dfrow = ['name', 'age', 'sex', 'height', 'length']

dfindex2 = [2,3,4,5,6,7]
dfrow2 = ['name', 'age', 'sex', 'height', 'length', 'weight']

d={'one': pd.Series(dfindex, index=dfrow),
    'two': pd.Series(dfindex2, index=dfrow2)
}
df=pd.DataFrame(d)
#df = pd.DataFrame(np.random.randn(5), index=dfindex, columns=dfcolumn)

df = pd.read_excel(r'/Users/zhangsicai/Desktop/Panda/grade.xlsx', sheet_name=0)


print(df)

summath = df['math'].sum()
print(summath)


web_stats = {'Day': [1,2,3,4,5,7],
             'Visitors': [43,34,65,56,29,76],
             'Bounce Rate': [65,67,78,65,45,52]
}

df = pd.DataFrame(web_stats)
df.set_index('Day', inplace=True)
'''
##read write csv
dfx = pd.read_csv('/Users/zhangsicai/Desktop/Panda/grade.csv')
dfx.set_index('Date', inplace=True)
dfx.rename(columns={'math': 'shuxue'}, inplace=True)
print(dfx['shuxue'])
#df['math'].to_csv('/Users/zhangsicai/Desktop/Panda/grade1.csv')


df = quandl.get('FMAC/HPI_TX', authtoken='HUg-EPXknoSxzbk26DMu')
fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
print(df.head())

print(df[0:2])
print(df['NSA Value'])
df.plot()
plt.show()

print(fiddy_states[0]['Name'])

'''
for dd in df['NSA Value'][1:]:
    print(dd)
'''

df1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 4],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004])
print(df1)
print(df3)

df4 = pd.merge (df1,df3, on=['Int_rate', 'HPI'], how='inner' )
print(df4)

# plt.scatter(np.arange(1,10,1),np.arange(10,19,1))

# plt.scatter(np.linspace(-3,3,10),np.linspace(-3,3,10))


#scattered plot
x = np.random.normal(1, 10, 500)
y = np.random.normal(1, 10, 500)

print(x)

plt.scatter(x, y, s=50, c='b', alpha=0.5)
plt.show()

