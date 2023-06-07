import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde
from scipy.stats import kurtosis

def oczyszczanie_danych(data):
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    filtered_data = [x for x in data if lower_bound <= x <= upper_bound]
    return filtered_data


tabela_pol = pd.read_csv("Projekt\\Dane1\\temp.csv",sep=';')
tabela_pol = tabela_pol.drop(tabela_pol.columns[-1],axis=1)


tabela_pol = tabela_pol.drop('Kod',axis=1)
tabela_pol = tabela_pol.drop('Nazwa',axis=1)
tabela_pol = tabela_pol.replace(',','.',regex = True) 
tabela_pol = tabela_pol.astype(float)
tabela_pol.columns = ['Y']
tabela_pol = tabela_pol['Y']

# tabela_pol = pd.DataFrame(oczyszczanie_danych(tabela_pol),columns=['Y'])
# tabela_pol = tabela_pol['Y']
# print(tabela_pol)

# kde = gaussian_kde(tabela_pol.ravel())
# x = np.linspace(tabela_pol.min(), tabela_pol.max(), 100)
# density = kde(x)

# # Oblicz kurtozę
# kurtoza = kurtosis(tabela_pol)

# print("Kurtoza:", kurtoza)

# # Wyświetl wykres
# plt.plot(x, density, color='blue', label='Krzywa gęstości')
# plt.hist(tabela_pol, bins='auto', density=True, alpha=0.5, color='gray', label='Histogram')
# plt.show()                

# tabela_pol.plot(kind='box', subplots=True,layout=(3,3),sharex=False,sharey=False)
# plt.show()

