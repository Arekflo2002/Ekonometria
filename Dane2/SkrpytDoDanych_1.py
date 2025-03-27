import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde
from scipy.stats import kurtosis
import scipy.stats as stats

def oczyszczanie_danych(tabela,nazwa):
    data = tabela[nazwa]
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    tabela = tabela[tabela[nazwa].between(lower_bound, upper_bound)]
    return tabela

def zamien_na_liczbe(value):
    if type(value) is float or type(value) is int:
        return value
    value = value.replace('−', '-')
    if 'k' in value:
        return float(value.replace('k', '')) * 1000
    if 'M' in value:
        return float(value.replace('M', '')) * 1000000
    else:
        return float(value)

def usuwanie_miast(value):
    if 'MIASTO' in value:
        return np.nan
    else:
        return value 


tabela_pol = pd.read_csv("Projekt\\Dane2\\a.csv",sep=";")
tabela_pol = tabela_pol.drop(tabela_pol.columns[-1],axis=1)
tabela_pol = tabela_pol.drop('Kod',axis=1)

nazwa = "Samobojstwa"
czy_zapisac = 1
czy_filtrowac = 0
czy_wsywietlic = not  czy_zapisac

# tabela_pol['Nazwa'] = tabela_pol['Nazwa'].apply(usuwanie_miast)
tabela_pol = tabela_pol.dropna(subset=tabela_pol.columns)
# tabela_pol = tabela_pol.drop('Nazwa',axis=1)
tabela_pol.columns = ['podregion',nazwa]


zapisanie = "Projekt\\Dane2\\"+nazwa+".xlsx"

tabela_pol = tabela_pol.replace(',','.',regex=True)
tabela_pol[nazwa] = tabela_pol[nazwa].astype(float)

tabela_gl = tabela_pol

if czy_filtrowac:
    tabela_pol = oczyszczanie_danych(tabela_pol,nazwa)


tabela_pol = tabela_pol.drop_duplicates(subset="podregion")
                              

if czy_zapisac:
    tabela_pol.to_excel(zapisanie,index=False)

tabela_gl = tabela_pol
tabela_pol = tabela_pol[nazwa]

kurtoza = kurtosis(tabela_pol)
wspZm = stats.variation(tabela_pol) 

print("Kurtoza:", kurtoza)
print("Wzzzzz:",wspZm)
print(len(tabela_pol))
if czy_wsywietlic:
    # Krzywa z moich danych
    kde = gaussian_kde(tabela_pol.ravel())
    x = np.linspace(tabela_pol.min(), tabela_pol.max(), 100)
    density = kde(x)

    # Krzywa rozkladu normalnego
    mu, std = np.mean(tabela_pol), np.std(tabela_pol)
    density_normal = stats.norm.pdf(x, mu, std)

    plt.plot(x, density_normal, color='red',alpha=0.5, label='Krzywa gęstości rozkładu normalnego')
    # Wyświetl wykres
    plt.plot(x, density, color='blue', label='Krzywa gęstości')
    plt.hist(tabela_pol, bins='auto', density=True, alpha=0.5, color='gray', label='Histogram')
    plt.show()   

    # tabela_pol.plot(kind='box', subplots=True,layout=(3,3),sharex=False,sharey=False)
    # plt.show()

