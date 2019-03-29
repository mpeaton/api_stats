import pytest
import numpy as np
from numpy_api_stats.numpy_stats import build_numpyAPI_query,build_api_list

_typelist = ['module','function','float','int','ufunc','builtin_function_or_method',
    'type','CClass','NoneType','PytestTester','RClass','bool','IndexExpression','_typedict',
    'str','nd_grid','_Feature','float','dict']
 
_api = [(x, type(np.__getattribute__(x))) for x in dir(np) if not x.startswith('__')] 


@pytest.mark.parametrize('l',[(['module']),(['module','type'])])
def test_build_query(l):
    api_list = build_api_list( _api , l )
    q = build_numpyAPI_query(api_list)
    assert(q)
