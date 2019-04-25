from numpy_api_stats import numpy_visitor as nv
from scipy.linalg import basic

V = nv.NumpyVisitor()

V(basic)

print(V.get_calls())
print(V.imports)
print(V.importfroms)
print(V.get_imports())
print(V.get_importfroms())
