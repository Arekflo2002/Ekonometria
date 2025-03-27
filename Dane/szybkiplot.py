import pandas as pd
import matplotlib.pyplot as plt


tabela = pd.read_excel("Projekt\\Dane\\Tabela_zapasowa.xlsx")


kolumny = ['X1','X2','X4','X5','X6']

tabela = tabela.drop(tabela.columns.difference(kolumny),axis=1)

tabela.columns = ['X1','X2','X3','X4','Y']
scatter = pd.plotting.scatter_matrix(tabela,marker = 'o',s=25,diagonal='kde',density_kwds={'linewidth': 2.5,'color':'navy'},figsize=(9,8),alpha=0.9)
for ax in scatter.ravel():
    ax.set_xticks([])
    ax.set_yticks([])
plt.savefig('Projekt\\Dane\\Scatter_matrix')
plt.show()

