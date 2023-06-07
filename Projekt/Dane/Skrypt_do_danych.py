import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import math 
import scipy.stats as stats

""" 
    Wczytywanie danych
"""

# emisja = pd.read_csv("Projekt\Dane\Emisja_zanieczyszczenSO2.csv",sep=';')
# emisja = emisja.drop(emisja.columns[-1],axis=1)

# przestepstwa = pd.read_csv("Projekt\Dane\Przestepstwa.csv",sep=";")
# przestepstwa = przestepstwa.drop(przestepstwa.columns[-1],axis=1)

# naklady_inwestycyjne = pd.read_csv("Projekt\\Dane\\Nakłady.csv",sep=";")
# naklady_inwestycyjne = naklady_inwestycyjne.drop(naklady_inwestycyjne.columns[-1],axis=1)

# poszkodowani = pd.read_csv("Projekt\Dane\Poszkodowani.csv",sep=";")
# poszkodowani = poszkodowani.drop(poszkodowani.columns[-1],axis=1)

# wynalazki  = pd.read_csv("Projekt\Dane\Wynalazki.csv",sep=";")
# wynalazki = wynalazki.drop(wynalazki.columns[-1],axis=1)

# bezrobocie = pd.read_csv("Projekt\Dane\Bezrobocie.csv",sep=";")
# bezrobocie = bezrobocie.drop(bezrobocie.columns[-1],axis=1)

wynagrodzenie = pd.read_csv("Projekt\Dane1\wynagr_miasta.csv",sep=";")
wynagrodzenie = wynagrodzenie.drop(wynagrodzenie.columns[-1],axis=1)

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
    data += 2000
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1
    lower_bound = q1 - 2 * iqr
    upper_bound = q3 + 1 * iqr
    filtered_data = [x for x in data if lower_bound <= x <= upper_bound]
    return filtered_data

# lista = [emisja,przestepstwa,naklady_inwestycyjne,poszkodowani,wynalazki,bezrobocie]

tabela_pol = wynagrodzenie

# for element in lista:
    # tabela_pol = pd.merge(tabela_pol, element,on=["Kod","Nazwa"])

tabela_pol = tabela_pol.drop('Kod',axis=1)
tabela_pol = tabela_pol.drop('Nazwa',axis=1)
# tabela_pol.columns = ['Y','X1','X2','X3','X4','X5','X6']
tabela_pol = tabela_pol.replace(',','.',regex = True) 
tabela_pol = tabela_pol.astype(float)


# tabela_pol = remove_outliers_and_create_dataframe(tabela_pol)

tabela_pol = tabela_pol.dropna(subset=tabela_pol.columns)
tabela_pol.to_excel("Projekt\\Dane\\tabela_polaczona1.xlsx",index=False)

scatter = pd.plotting.scatter_matrix(tabela_pol,marker = 'o',s=15,hist_kwds={'bins':7,'color':'navy'},figsize=(9,8),alpha=0.9)
for ax in scatter.ravel():
    ax.set_xticks([])
    ax.set_yticks([])
# plt.savefig('Projekt\\Dane\\Scatter_matrix')
# plt.show()

tabela_pol.plot(kind='box', subplots=True,layout=(3,3),sharex=False,sharey=False)
plt.tight_layout()
plt.show()

