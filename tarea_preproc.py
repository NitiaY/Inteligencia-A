# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 17:47:36 2020

@author: Usuario
"""

import numpy as np
import pandas as pd


iris =pd.read_csv('iris.csv')
iris = iris.drop('Id',axis=1)
#print(iris)


x = np.array(iris.drop(['Species'],1))
y = np.array(iris['Species'])

#print(x)
#print(y)

from sklearn.preprocessing import Imputer
imp = Imputer(missing_values=np.NaN, strategy='mean')
matriz_imputer = imp.fit_transform(x)
print(matriz_imputer)


from sklearn.preprocessing import Normalizer
nor = Normalizer()
matriz_nor = nor.fit(matriz_imputer)
matriz_nor.transform(x)
print(matriz_nor)

from sklearn.preprocessing import StandardScaler
ssa = StandardScaler()
matriz_ssa = ssa.fit(matriz_imputer)
matriz_ssa.transform(x)
print(matriz_ssa.transform(x))






