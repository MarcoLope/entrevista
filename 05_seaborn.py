import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


indice = np.arange(100)
col1 = np.random.randn(100) * 100
datos = np.array([indice, col1])

# ax = sns.histplot(data=datos[1],kde=True)
# sns.set_style('ticks') #white whitegrid, 
# sns.set_style('white')
# ax = sns.kdeplot(data=datos[1])
# ax = sns.histplot(data=datos[1],kde=True, palette='seismic') #'coolwarm'
# ax = sns.scatterplot(x=datos[0],y=datos[1], palette='seismic')
# plt.title('Grafica');
# plt.show()

