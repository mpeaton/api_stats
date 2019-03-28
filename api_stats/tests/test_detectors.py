import re
import pytest
from api_stats.numpy_api_stats.numpy_stats import detect_fun,detect_mod,detect_float,detect_int,detect_ufunc

@pytest.mark.parametrize('m,s',[('linalg','from numpy.linalg import svd'),('linalg','import numpy.linalg as')])
def test_mod(m,s):
    assert(re.match(detect_mod(m),s))
  
@pytest.mark.parametrize('f,s',[('sqrt','np.sqrt(2)'), ('abs','numpy.abs(1)')])
def test_fun(f,s):
    rstring = detect_fun(f)
    r = re.search( rstring ,s)
    assert(r)

@pytest.mark.parametrize('f,s',[('e','np.e'),('e','x = np.e + 1')])
def test_float(f,s):
    assert(re.search(detect_float(f),s))

@pytest.mark.parametrize('f,s',[('SHIFT_UNDERFLOW','if np.SHIFT_UNDERFLOW:'),('FPE_INVALID','if numpy.FPE_INVALID:')])
def test_int(f,s):
    assert(re.search(detect_int(f),s))

@pytest.mark.parametrize('f,s',[('add','np.add(something,something_else')])
def test_ufunc(f,s):
    assert(re.search(detect_ufunc(f),s))