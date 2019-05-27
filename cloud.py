from scipy.io import mmread
from scipy import linalg

data = mmread('bcsstk17.mtx')
B = data.todense()
print(B)

C=linalg.inv(B)
print(C)

