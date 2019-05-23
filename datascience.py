from scipy.io import mmread
from scipy import linalg

data = mmread('bcsstk17.mtx')
print(data)
B = data.todense()
print(B)

C=linalg.det(B)
print(C)