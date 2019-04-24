
from numpy_api_stats import numpy_visitor as nv      

import sys
sys.path.insert(0,'/Users/mpeaton/SCIPY')

from scipy.linalg import basic


V = nv.NumpyVisitor(None,None)

V(basic)
print(V.get_calls())           

print(V.imports)
print(V.importfroms)
print(V.get_imports())
print(V.get_importfroms())