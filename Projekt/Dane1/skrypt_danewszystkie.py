import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import math 
import scipy.stats as stats

""" 
    Wczytywanie danych
"""

X1 = pd.read_csv("Projekt\\Dane1\\Bezrobocie.csv",sep=';')
X2 = pd.read_csv("Projekt\\Dane1\\Dochod.csv",sep=';')
X3 = pd.read_csv("Projekt\\Dane1\\Drogi.csv",sep=';')
X4 = pd.read_csv("Projekt\\Dane1\\Obciazenie_dem.csv",sep=';')
X5 = pd.read_csv("Projekt\\Dane1\\Poszkodowani.csv",sep=';')
X6 = pd.read_csv("Projekt\\Dane1\\Przestepstwa.csv",sep=';')
X7 = pd.read_csv("Projekt\\Dane1\\Przyrost.csv",sep=';')
X8 = pd.read_csv("Projekt\\Dane1\\Przyrost1000.csv",sep=';')
X9 = pd.read_csv("Projekt\\Dane1\\Samoboje.csv",sep=';')
X10 = pd.read_csv("Projekt\\Dane1\\Wydatki.csv",sep=';')
X11 = pd.read_csv("Projekt\\Dane1\\Wypadki.csv",sep=';')

lista = [X1,X2,X3,X4,X5,X6,X7,X8,X9,X10,X11]
for el in lista:
    el = el.drop(el.columns[-1],axis=1,inplace=True)
# emisja = emisja.drop(emisja.columns[-1],axis=1)
"""
    Wyrzucanie braków w danych oraz łączenie w jedna tabele 
 """

# Funckja do wyrzucania danych odstajacyhc
def remove_outliers_and_create_dataframe(df):
    filtered_data = df.copy()  # Tworzenie kopii oryginalnego DataFrame dla przefiltrowanych danych
    for column in df.columns:
        column_data = df[column]
        # Wywołanie funkcji usuwania outlierów na wybranej kolumnie
        filtered_column_data = filtering(column_data)
        filtered_data[column] = pd.Series(filtered_column_data)  # Dodanie przefiltrowanej kolumny do nowego DataFrame
    return filtered_data

def filtering(data):
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1
    lower_bound = q1 - 2 * iqr
    upper_bound = q3 + 1 * iqr
    filtered_data = [x for x in data if lower_bound <= x <= upper_bound]
    return filtered_data


tabela_pol = X1
print(tabela_pol)

for element in lista[1:]:
    tabela_pol = pd.merge(tabela_pol, element,on=["Kod","Nazwa"])

tabela_pol = tabela_pol.drop('Kod',axis=1)
tabela_pol = tabela_pol.drop('Nazwa',axis=1)
tabela_pol.columns = ['X1','X2','X3','X4','X5','X6','X7','X8','X9','X10','X11']
tabela_pol = tabela_pol.replace(',','.',regex = True) 
tabela_pol = tabela_pol.astype(float)


# tabela_pol = remove_outliers_and_create_dataframe(tabela_pol)

tabela_pol = tabela_pol.dropna(subset=tabela_pol.columns)
tabela_pol.to_excel("Projekt\\Dane\\tabela_polaczona1.xlsx",index=False)

scatter = pd.plotting.scatter_matrix(tabela_pol,marker = 'o',s=15,hist_kwds={'bins':7,'color':'navy'},figsize=(9,8),alpha=0.9)
for ax in scatter.ravel():
    ax.set_xticks([])
    ax.set_yticks([])
plt.savefig('Projekt\\Dane\\Scatter_matrix')
plt.show()

tabela_pol.plot(kind='box', subplots=True,layout=(3,4),sharex=False,sharey=False)
plt.savefig("Projekt\\Dane\\Boxplot")
plt.tight_layout()
plt.show()

tabela_pol = tabela_pol.dropna(subset=tabela_pol.columns)
tabela_pol.to_excel("Projekt\\Dane\\tabela_polaczona1.xlsx",index=False)
