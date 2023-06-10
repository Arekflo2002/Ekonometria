import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import math 
import scipy.stats as stats
import os


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

""" 
    Wczytywanie danych
"""


""" 
    Pamietaj zeby usunac polaczona tabele bo przypal!!!!!!
"""  


folder_path = "Projekt\\Dane2"

xlsx_files = [file for file in os.listdir(folder_path) if file.endswith('xlsx')]

lista = []  # Lista do przechowywania wczytanych DataFrame'ów

for file in xlsx_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_excel(file_path)
    lista.append(df)


czy_rysowac = 1

tabela_pol = lista[0]

for el in lista[1:]:
    tabela_pol = tabela_pol.merge(el.drop_duplicates(subset="podregion"), on="podregion", how="inner")




tabela_pol = tabela_pol.dropna(subset=tabela_pol.columns)
print(len(tabela_pol))

# tabela_pol = tabela_pol.drop(tabela_pol.columns[0],axis=1)
tabela_pol.columns = ['X1','X2','X3','X4','X5','X6','X7','X8','X9','X10','X11','X12','X13']

tabela_pol = tabela_pol.astype(float)

tabela_pol = remove_outliers_and_create_dataframe(tabela_pol)
tabela_pol = tabela_pol.dropna(subset=tabela_pol.columns)

for nazwa,kol in tabela_pol.items():
    kurtoza = stats.kurtosis(kol)
    wspZm = stats.variation(kol)
    print(nazwa+": K : ",kurtoza,", WZ: ",wspZm)   

tabela_pol.to_excel("Projekt\\Dane2\\tabela_polaczona_braki2.xlsx",index=False)

if czy_rysowac:
    scatter = pd.plotting.scatter_matrix(tabela_pol,marker = 'o',s=15,hist_kwds={'bins':7,'color':'navy'},figsize=(9,8),alpha=0.9)
    for ax in scatter.ravel():
        ax.set_xticks([])
        ax.set_yticks([])
    plt.savefig('Projekt\\Dane1\\Scatter_matrix')
    # plt.show()

    # tabela_pol.plot(kind='box', subplots=True,layout=(4,3),sharex=False,sharey=False)
    # plt.tight_layout()
    # plt.show()

print(len(tabela_pol))
# Tworzenie macierzy korelacji dat
tabela = tabela_pol.drop(tabela_pol.columns[0],axis=1)
corr_matrix = tabela.corr()

print(corr_matrix)

corr_sum = corr_matrix.abs()
corr_sum = corr_sum.sum()

print(corr_sum)

