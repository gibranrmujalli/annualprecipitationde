#extract the station's name with the highest precipitation by state
"""
Niederschlag: vieljährige Mittelwerte 1981 - 2010
aktueller Standort
"""
import pandas as pd

df = pd.read_csv('niederschlag stadt.txt', decimal=',',sep='\t')



print('This small software will extract the station with the highest yearly precipitation (mm) by Busdesland in Germany.')
print('please select the bundesland from the following list:')
a=df['Bundesland'].unique().tolist()
for x in range(len(a)):
    print(a[x])
z=input('write the selected Bundesland: ')
print('you have selected ',z)
x=df.groupby('Bundesland', sort = False,as_index = False).max()
#print(x[x['Bundesland']==z])
x=x[x['Bundesland']==z]
b=x['Name der Station'].values[0]
#print(b)
c=x['Jahr'].values[0]

print('The station with the highest precipitation per year of ',z,' is ',b,' with a precipitation of',c,' mm/a')
#Jahr
df2=df[df['Bundesland']==z]
df2 = df2[['Name der Station', 'Jahr']]

df2.to_csv(z+'_out.csv', index=False) 

