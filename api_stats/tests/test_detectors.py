import re
import pytest
from api_stats.numpy_api_stats.numpy_stats import detect_fun,detect_mod

@pytest.mark.parametrize('m,s',[('linalg','from numpy.linalg import svd'),('linalg','import numpy.linalg as')])
def test_mod(m,s):
    assert(re.match(detect_mod(m),s))
  
@pytest.mark.parametrize('f,s',[('sqrt','np.sqrt(2)'), ('abs','numpy.abs(1)')])
def test_fun(f,s):
    rstring = detect_fun(f)
    r = re.match( rstring ,s)
    assert(r)