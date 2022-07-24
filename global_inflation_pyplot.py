import matplotlib.pyplot as plt
import matplotlib as mpl
#import numpy as np
import pandas as pd

df = pd.DataFrame({
    "date":["2021-05","2021-06","2021-07","2021-08","2021-09","2021-10","2021-11","2021-12","2022-01","2022-02","2022-03","2022-04","2022-05","2022-06"],
    'Can':[3.600294, 3.061224, 3.717201, 4.087591, 4.382761, 4.654545, 4.720407, 4.803493, 5.137482, 5.687545, 6.661891, 6.771204, 7.730496, 8.132957],
    'Ita':[1.264591, 1.263363, 1.94742, 2.038835, 2.541544, 3.02439, 3.710938, 3.898635, 4.840271, 5.705996, 6.460945, 5.955812, 6.820365, 7.965451],
    'Jpn':[-0.8, -0.5, -0.3, -0.4, 0.2, 0.1, 0.6, 0.8, 0.5, 0.9, 1.2, 2.5, 2.5, 2.1],
    'Gbr':[2.1, 2.4, 2.1, 3, 2.9, 3.8, 4.6, 4.8, 4.9, 5.5, 6.2, 7.8, 7.9, 8.2],
    'Usa':[4.992707, 5.391451, 5.365475, 5.251272, 5.390349, 6.221869, 6.809003, 7.036403, 7.479873, 7.871064, 8.542456, 8.25863, 8.581511, 9.059758],
    'Chin':[1.3, 1.1, 1,0.8,0.7,1.5,2.3,1.5,0.9,0.9,1.5,2.1,2.1,2.5],
    #'Rus':[6.014352, 6.511526,6.469069,6.692744,7.408086, 8.135334, 8.403767, 8.393015, 8.737564, 9.158359, 16.69844, 16.69844, 16.69844, 16.69844],
    'OECD':[ 3.850541, 4.04031, 4.228713, 4.347535, 4.59232, 5.231059, 5.860974, 6.5539, 7.177954, 7.755692, 8.767221, 9.17658, 9.646049,9.646049]
})
#y = np.loadtxt('World Inflation Data.csv')

df = df.set_index('date')
df.plot(kind='line')
print(df)

plt.title('Inflation from May 2021 - Jun 2022')
plt.ylabel('CPI (consumer price index)')
plt.xlabel('Date')

#x = np.linspace(0, 20, 100)
#plt.plot(x, np.sin(x))
plt.show()