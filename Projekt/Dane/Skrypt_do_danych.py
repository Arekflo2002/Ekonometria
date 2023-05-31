import pandas as pd 
import numpy as np

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

lista = [malzenstwa,naklady_inwestycyjne,poszkodowani,skolaryzacja,bezrobocie,wynagrodzenie]

tabela_pol = emisja

for element in lista:
    tabela_pol = pd.merge(tabela_pol, element,on=["Kod","Nazwa"])

tabela_pol = tabela_pol.dropna(subset=tabela_pol.columns)
tabela_pol.to_excel("Projekt\\Dane\\tabela_polaczona.xlsx",index=False)

x = tabela_pol
print(len(x))
print(x.columns)
print(x.head())

