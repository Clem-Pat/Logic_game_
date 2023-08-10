import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

L = [20, 40, 60, 80]
M = [10, 5, 1, 0]

modeleReg=LinearRegression()
modeleReg.fit([L, M])
regression_lin = modeleReg.predict(M)

R = modeleReg.score(L,M)
print(R)

plt.plot(L, M)
plt.plot(L, regression_lin)
plt.xlabel('Yuka')
plt.ylabel('Equivalent CO2')
plt.show()