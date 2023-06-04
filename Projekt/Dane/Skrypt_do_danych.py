import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

""" 
    Wczytywanie danych
"""

emisja = pd.read_csv("Projekt\Dane\Emisja_zanieczyszczenSO2.csv",sep=';')
emisja = emisja.drop(emisja.columns[-1],axis=1)

przestepstwa = pd.read_csv("Projekt\Dane\Przestepstwa.csv",sep=";")
przestepstwa = przestepstwa.drop(przestepstwa.columns[-1],axis=1)

naklady_inwestycyjne = pd.read_csv("Projekt\\Dane\\Nakłady.csv",sep=";")
naklady_inwestycyjne = naklady_inwestycyjne.drop(naklady_inwestycyjne.columns[-1],axis=1)

poszkodowani = pd.read_csv("Projekt\Dane\Poszkodowani.csv",sep=";")
poszkodowani = poszkodowani.drop(poszkodowani.columns[-1],axis=1)

wynalazki  = pd.read_csv("Projekt\Dane\Wynalazki.csv",sep=";")
wynalazki = wynalazki.drop(wynalazki.columns[-1],axis=1)

bezrobocie = pd.read_csv("Projekt\Dane\Bezrobocie.csv",sep=";")
bezrobocie = bezrobocie.drop(bezrobocie.columns[-1],axis=1)

wynagrodzenie = pd.read_csv("Projekt\Dane\Wynagrodzenia.csv",sep=";")
wynagrodzenie = wynagrodzenie.drop(wynagrodzenie.columns[-1],axis=1)

"""
    Wyrzucanie braków w danych oraz łączenie w jedna tabele 
 """

lista = [emisja,przestepstwa,naklady_inwestycyjne,poszkodowani,wynalazki,bezrobocie]

tabela_pol = wynagrodzenie

for element in lista:
    tabela_pol = pd.merge(tabela_pol, element,on=["Kod","Nazwa"])

tabela_pol = tabela_pol.dropna(subset=tabela_pol.columns)
# tabela_pol.to_excel("Projekt\\Dane\\tabela_polaczona11.xlsx",index=False)

tabela_pol = tabela_pol.drop('Kod',axis=1)
tabela_pol = tabela_pol.drop('Nazwa',axis=1)
tabela_pol.columns = ['Y','X1','X2','X3','X4','X5','X6']
tabela_pol = tabela_pol.replace(',','.',regex = True)
tabela_pol = tabela_pol.astype(float)

scatter = pd.plotting.scatter_matrix(tabela_pol,marker = 'o',s=15,hist_kwds={'bins':7,'color':'navy'},figsize=(9,8),alpha=0.9)
for ax in scatter.ravel():
    ax.set_xticks([])
    ax.set_yticks([])
plt.savefig('Projekt\\Dane\\Scatter_matrix')
plt.show()

tabela_pol.plot(kind='box', subplots=True,layout=(3,3),sharex=False,sharey=False)
plt.tight_layout()
plt.show()

