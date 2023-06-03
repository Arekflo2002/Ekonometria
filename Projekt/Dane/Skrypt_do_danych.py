import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

""" 
    Wczytywanie danych
"""

emisja = pd.read_csv("Projekt\Dane\Emisja_zanieczyszczen.csv",sep=';')
emisja = emisja.drop(emisja.columns[-1],axis=1)

malzenstwa = pd.read_csv("Projekt\Dane\Małżeństwa.csv",sep=";")
malzenstwa = malzenstwa.drop(malzenstwa.columns[-1],axis=1)

naklady_inwestycyjne = pd.read_csv("Projekt\\Dane\\Naklady_inwestycyjne.csv",sep=";")
naklady_inwestycyjne = naklady_inwestycyjne.drop(naklady_inwestycyjne.columns[-1],axis=1)

poszkodowani = pd.read_csv("Projekt\Dane\Poszkodowani_przyPracy.csv",sep=";")
poszkodowani = poszkodowani.drop(poszkodowani.columns[-1],axis=1)

skolaryzacja  = pd.read_csv("Projekt\Dane\Skolaryzacja.csv",sep=";")
skolaryzacja = skolaryzacja.drop(skolaryzacja.columns[-1],axis=1)

bezrobocie = pd.read_csv("Projekt\Dane\Stopa_bezrobocia.csv",sep=";")
bezrobocie = bezrobocie.drop(bezrobocie.columns[-1],axis=1)

wynagrodzenie = pd.read_csv("Projekt\Dane\Wynagrodzenie.csv",sep=";")
wynagrodzenie = wynagrodzenie.drop(wynagrodzenie.columns[-1],axis=1)

"""
    Wyrzucanie braków w danych oraz łączenie w jedna tabele 
 """

lista = [emisja,malzenstwa,naklady_inwestycyjne,poszkodowani,skolaryzacja,bezrobocie]

tabela_pol = wynagrodzenie

for element in lista:
    tabela_pol = pd.merge(tabela_pol, element,on=["Kod","Nazwa"])

tabela_pol = tabela_pol.dropna(subset=tabela_pol.columns)
# tabela_pol.to_excel("Projekt\\Dane\\tabela_polaczona.xlsx",index=False)

tabela_pol = tabela_pol.drop('Kod',axis=1)
tabela_pol = tabela_pol.drop('Nazwa',axis=1)
tabela_pol.columns = ['Y','X1','X2','X3','X4','X5','X6']
tabela_pol = tabela_pol.replace(',','.',regex = True)
tabela_pol = tabela_pol.astype(float)

scatter = pd.plotting.scatter_matrix(tabela_pol,marker = 'o',s=12,hist_kwds={'bins':20},figsize=(9,8),alpha=0.4)
for ax in scatter.ravel():
    ax.set_xticks([])
    ax.set_yticks([])
plt.show()