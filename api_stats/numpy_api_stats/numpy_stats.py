import numpy as np
from pandas import read_csv as pd_read_csv
from pandas import DataFrame
import matplotlib.pyplot as plt
#from google.cloud import bigquery
def select(api,ttype):
        if ttype=='function':
            return [(x[0],x[1].__name__) for x in api if x[1] is type(lambda x: x)]
        elif ttype=='module':
            return  [ (x[0],x[1].__name__) for x in api if x[1] is type(np.char)]
        elif ttype=='int':
            return  [ (x[0],x[1].__name__) for x in api if x[1] is type(np.CLIP)] 
        elif ttype=='float':
            return  [ (x[0],x[1].__name__) for x in api if x[1] is type(np.e)]
        elif ttype=='ufunc':
            return  [ (x[0],x[1].__name__) for x in api if x[1] is type(np.add)]
        elif ttype=='builtin_function_or_method':
            return  [ (x[0],x[1].__name__) for x in api if x[1] is type(np.array)]
        elif ttype=='type':
            return  [ (x[0],x[1].__name__) for x in api if x[1] is type(np.int8)]
        else:
            return NotImplementedError

def build_api_list(api,typelist=['ufunc']):
    

    api_list = [(x[0],x[1].__name__) for x in api]

    # Add main numpy module for nomalization
    api_list.append(('numpy','module'))

    df_api = DataFrame(api_list,columns = ['label','type'])

    df_api.set_index('type',inplace=True)

    df_api_list = df_api.loc[typelist].reset_index()
    return [ (r[1].label,r[1].type) for r in df_api_list.iterrows()]

class API_QUERY_FACTORY:
    
    _typelist = ['module','function','float','int','ufunc','builtin_function_or_method',
    'type','CClass','NoneType','PytestTester','RClass','bool','IndexExpression','_typedict',
    'str','nd_grid','_Feature','dict']
    
    _api = [(x, type(np.__getattribute__(x))) for x in dir(np) if not x.startswith('__')] 
   
    def __init__(self,api=None,api_list=None,typelist=None,content_table=None,file_table=None):
        
        if api: self._api = api
        else: api = self._api 
        
        if  typelist: self._typelist=typelist
        else: typelist=self._typelist
        
        if api_list:
            self.api_list=api_list
        else:
            api_list = build_api_list(api,typelist)

        if content_table: self.content_table=content_table
        else: self.content_table = '[bigquery-public-data:github_repos.contents]'

        if file_table: self.file_table=file_table
        else: self.file_table = '[bigquery-public-data:github_repos.files]'

        self.query =  build_numpyAPI_query( api_list, content_table = nest_table(
                        build_py_content(content_table_name=self.content_table,
                        join=join_py(file_table = self.file_table))
                                     )) 
        self.count_query = build_countAPIs(api_list,api_table='[apt-footing-235018.NumpyAPI.latest_numpy]')

def groupby(x):
    y = {}
    #group a list of tuples by second index
    for xx in x:
        if xx[1] in y:
            y[xx[1]].append(xx[0])
        else: y[xx[1]] = [xx[0]]
    return y

def groupdiff(x1,x2):
    diff={}
    for k in  x1.keys() & x2.keys():
        ldiff = list(set(x1[k]) - set(x2[k]))
       # rdiff = list(set(x2[k]) - set(x1[k]))
       # diff[k] = (ldiff,rdiff)
        diff[k] = ldiff
       # if (ldiff,rdiff) == ([],[]):
       #     diff.pop(k)
    for k in x1.keys() - x2.keys():
        diff[k] = x1[k]
    #for k in x2.keys() - x1.keys():
    #    diff[k] = x2[k]
    #return diff

def run_legacy_query(query):

    client = bigquery.Client()
    
    # Set use_legacy_sql to True to use legacy SQL syntax.
    job_config = bigquery.QueryJobConfig()
    job_config.use_legacy_sql = True

    query_job = client.query(
        query,
        # Location must match that of the dataset(s) referenced in the query.
        location='US',
        job_config=job_config)  # API request - starts the query
    
    return query_job

def run_standard_query(query):
    
    client = bigquery.Client()

    job_config = bigquery.QueryJobConfig()
    job_config.use_legacy_sql = False
    
    query_job = client.query(
        query,
        # Location must match that of the dataset(s) referenced in the query.
        location='US',
        job_config=job_config)  # API request - starts the query
    
    return query_job

def print_results(job):
    # Print the results.
    for row in job:  # API request - fetches results
        print(row)

# def read_results(filename = None):
#     if filename:
#         return pd_read_csv(filename)
#     else:
#         return 'this'

def plot_results(results,savefig=False,filename='results.png',dpi=250):
#    import matplotlib.pyplot as plt; plt.rcdefaults()
    import matplotlib.pyplot as plt
    
    r = results.T
    r2 = r.loc[r[0]>0].sort_values(0,ascending=False)
    r2.index = [ f.split('_')[-2] for f in list(r2.index)]

    r2 = r2[:100]
    y_pos = np.arange(len(r2))
    calls = r2[0]
    
    fig1 = plt.bar(y_pos, calls, align='center', alpha=0.5,log=True)
    plt.xticks(y_pos,r2.index,rotation='vertical',fontsize=4)
    plt.ylabel('Calls')
    plt.title('API calls from github query')

    if savefig:
        fig1 = plt.gcf() 
        fig1.savefig(filename, dpi=dpi)
    plt.show()

def plot_bar_repo(df):
    N=100
    fig, ax = plt.subplots()
    p=[]
    for r in np.arange(len(df)):
        rname = df.index[r]
        p.append(ax.bar(np.arange(N),df.iloc[r,:N]*100,log=True))
        ax.legend( p , df.index,loc=1)
    plt.xticks(np.arange(N),[ f.split('_')[-2] for f in list(df.columns[:N])],rotation='vertical',fontsize=4)
    plt.ylabel('log %')
    plt.title('Percentage Numpy API Calls')
    return fig

def build_getAPItable_query():
    return '''
SELECT functions 
FROM [apt-footing-235018:NumpyAPI.functions] f
ORDER BY f.functions
'''

def build_py_query(file_table = '[bigquery-public-data:github_repos.sample_files]'):
    w1string = f'''(
f.path LIKE '%.py' 
OR
f.path LIKE '%.ipynb'
OR
f.path LIKE '%.pyx'
) '''
    return '\n'.join(['SELECT', 'repo_name, path, f.id', 'FROM',file_table + ' AS f','WHERE',w1string])

def nest_table(t):
    return '('+t+')'

def build_py_content(content_table_name='[bigquery-public-data:github_repos.sample_contents]',join=''):
    return '\n'.join(['SELECT','c.id, content,binary,repo_name,path','FROM',content_table_name + ' AS c',join])

def join_py(file_table = '[bigquery-public-data:github_repos.sample_files]'):
    return '\n'.join(['INNER JOIN',nest_table(build_py_query(file_table = file_table))+' AS p','ON','c.id = p.id','WHERE binary = False'])

def get_numpyAPI_function_list(client):
    query_job = client.query( build_getAPItable_query() )  # API request
    df = query_job.result().to_dataframe()
    return [r[1][0] for r in df.iterrows()]

# The vast majority of numpy imports are as np.  As such the following detectors are predicated on that namespace.
# Lookahead and Lookbehind regex may be used to reduce false negatives, however counts of module import should at
# be correct.  (
# https://medium.com/google-cloud/naming-conventions-in-python-import-statements-a-bigquery-adventure-using-the-github-db-dump-d900159ab680]
def detect_fun(f):
    return  f'(np\.|numpy\.){f}\(\s?[A-Za-z0-9_.\(\)]*\s?\)'

def detect_mod(m):
    if m=='numpy':
        return f'import\s+numpy'
    else:
        return f'(import\s+numpy\.{m}|from\s+numpy\s+import\s+{m}|from\s+numpy\.{m} import\s+[A-za-z0-9_.]+)'

def detect_float(f):
    # if f.lower()=='nan':
    #     return f'(np\.|numpy\.(nan|NaN|NAN)'
    # elif f.lower()=='inf':
    #     return f'(np\.|numpy\.(Inf|inf)'
    # else:
    return  f'(np\.|numpy\.){f}\s*[\*\+\-\/]?'

def detect_int(f):
    return  f'(np\.|numpy\.){f}'

def detect_ufunc(f):
    return f'(np\.|numpy\.){f}\(\s?[A-Za-z0-9_.,\(\)]*\s?\)'

def detect_builtin(f):
    return f'(np\.|numpy\.){f}\(\s?[A-Za-z0-9_.\(\){{}}\[\]]*\s?\)'

def detect_type(f):
    return f'(np\.|numpy\.){f}[\s\)\]}}\+\-\/\*]+'

def detect_misc(f):
    if f=='c_':
        return r'(np\.|numpy\.)c_\.(axis|concatenate\(|makemat\(|matrix|ndmin|trans1d)'
    elif f=='newaxis':
        return r'(np\.|numpy\.)newaxis'
    elif f=='test':
        return r'(np\.|numpy\.)test\('
    elif f=='r_':
        return r'(np\.|numpy\.)r_\.(axis|concatenate\(|makemat\(|matrix|ndmin|trans1d)'
    elif f=='little_endian':
        return r'(from\s+numpy\s+import\s+little_endian|(numpy\.|np\.)little_endian)'
    elif f in ['s_','index_exp']:
        return f'(np\.|numpy\.){f}(\.\(maketuple|\[\s?[0-9]?:[0-9]?:?[0-9]?\])'
    elif f in ['cast']:
        return f'(np\.|numpy\.){f}'
    elif f=='nbytes':
        bstring='|'.join([ x.__name__ for x in np.nbytes.keys() ])  
        return f'(np\.|numpy\.)nbytes\[\s?({bstring})\s?\]'
    elif f in ['numarray','oldnumeric','UFUNC_PYVALS_NAME']:
        return f'(np\.|numpy\.){f}'
    elif f in ['mgrid','ogrid']:
        return f'(np\.|numpy\.){f}\[\s?[0-9]\s?:\s?[0-9]\s?,\s?[0-9]\s?:\s?[0-9]\s?\]'
    elif f in ['print_function','absolute_import','division']:
        return f'(np\.|numpy\.){f}'
    elif f=='sctypeDict':
        #TODO FIX BETTER
        return f'(np\.|numpy\.){f}\['
        #tstring='|'.join([ str(x) if type(x) is int else f'\\\'{x}\\\'' for x in np.sctypeDict.keys() ])
       # tstring = tstring.replace('?','\?')
        #return f'(np\.|numpy\.){f}\[\s?{tstring}\s?\]' 
    elif f=='sctypes': 
        #TODO FIX BETTER
        return f'(np\.|numpy\.){f}\['
        #tstring='|'.join([ f'\\\'{x}\\\'' for x in np.sctypes.keys()])
        #return f'(np\.|numpy\.){f}\[\s?({tstring})\s?\]'
    elif f=='typeDict': 
        #TODO FIX BETTER
        return f'(np\.|numpy\.){f}\['
        #tstring='|'.join([ str(x) if type(x) is int else f'\\\'{x}\\\'' for x in np.typeDict.keys() ])
        #return f'(np\.|numpy\.){f}\[\s?{tstring}\s?\]'  
    elif f=='typecodes':
        #TODO FIX BETTER
        return f'(np\.|numpy\.){f}\['
        #tstring='|'.join([ f'\\\'{x}\\\'' for x in np.typecodes.keys()])
        #return f'(np\.|numpy\.){f}\[\s?({tstring})\s?\]' 
    elif f=='sctypeNA': 
        #TODO FIX BETTER
        return f'(np\.|numpy\.){f}\['
        #tstring='|'.join([ f'\\\'{x}\\\'' if type(x) is str else f'(np\.|numpy\.){x.__name__}' for x in np.sctypeNA.keys()])
        #tstring = tstring.replace('?','\?')
        #return f'(np\.|numpy\.){f}\[\s?{tstring}\s?\]' 
    elif f=='typeNA': 
        #TODO FIX BETTER
        return f'(np\.|numpy\.){f}\['
        #tstring='|'.join([ f'\\\'{x}\\\'' if type(x) is str else f'(np\.|numpy\.){x.__name__}' for x in np.typeNA.keys()])
        #tstring = tstring.replace('?','\?') 
        #return f'(np\.|numpy\.){f}\[\s?{tstring}\s?\]'
    else:
        print("What the type you talkin' bout?")
        return NotImplementedError
    

def build_cname(name,ttype):
    if name=='NaN': name='nan1'
    elif name=='NAN':name='nan2'
    elif name=='nan':name='nan3'
    elif name=='Inf':name='inf1'
    elif name=='inf':name='inf2'
    return '_'.join(['numpy',ttype,name])

def build_sql_regex(name,ttype, source_name = 'c.content'):
    if ttype=='function':
        regex = detect_fun(name)
        regex = regex.replace('\\','\\\\')
        return f'REGEXP_MATCH( {source_name},\'{regex}\' ) AS {build_cname(name,ttype)}' 
    
    elif ttype=='module':
        regex = detect_mod(name)
        regex = regex.replace('\\','\\\\')
        #import pdb; pdb.set_trace()
        return f'REGEXP_MATCH({source_name},\'{regex}\' ) AS {build_cname(name,ttype)}'
    
    elif ttype=='float':
        regex = detect_float(name)
        regex = regex.replace('\\','\\\\')
       # if name.lower()=='nan':import pdb;pdb.set_trace()
        return f'REGEXP_MATCH({source_name},\'{regex}\' ) AS {build_cname(name,ttype)}'
    
    elif ttype=='int':
        regex = detect_int(name)
        regex = regex.replace('\\','\\\\')
        return f'REGEXP_MATCH({source_name},\'{regex}\' ) AS {build_cname(name,ttype)}'

    elif ttype=='ufunc':
        regex = detect_ufunc(name)
        regex = regex.replace('\\','\\\\')
        return f'REGEXP_MATCH({source_name},\'{regex}\' ) AS {build_cname(name,ttype)}'
    
    elif ttype=='builtin_function_or_method':
        regex = detect_builtin(name)
        regex = regex.replace('\\','\\\\')
        return f'REGEXP_MATCH({source_name},\'{regex}\' ) AS {build_cname(name,ttype)}' 
    
    elif ttype=='type':
        regex = detect_type(name)
        regex = regex.replace('\\','\\\\')
        return f'REGEXP_MATCH({source_name},\'{regex}\' ) AS {build_cname(name,ttype)}' 
    
    elif ttype in ['CClass','NoneType','PytestTester','RClass','PytestTester','bool','IndexExpression',
    '_typedict','str','nd_grid','_Feature','dict']:
        regex = detect_misc(name)
        regex = regex.replace('\\','\\\\')
        return f'REGEXP_MATCH({source_name},\'{regex}\' ) AS {build_cname(name,ttype)}'  
    else:
        raise NotImplementedError 

def build_numpyAPI_query(api_list, content_table = '[bigquery-public-data:github_repos.sample_contents]'):
    qlist=[]
    source_name = 'c.content'
    for f in api_list:
        qlist.append(build_sql_regex(f[0],f[1]))

    #prepend the repo_name and path for key information
    qlist = ['repo_name','path'] + qlist 
    return '\n'.join(['SELECT',',\n'.join(qlist),f'FROM {content_table}'])


def build_countAPIs(api_list,api_table='None'):
    return 'SELECT\n'+',\n'.join([f'count(CASE WHEN {build_cname(*f)} THEN 1 END) AS {build_cname(*f)}_count' for f in api_list]) + f'\nFROM {api_table}'

if __name__ == '__main__':
   
    import os 

    os.environ['GOOGLE_APPLICATION_CREDENTIALS']='/Users/mpeaton/Downloads/apt-footing-235018-aeb185ac9e31.json' 
    api = [(x, type(np.__getattribute__(x))) for x in dir(np) if not x.startswith('__')] 
    
    apq = API_QUERY_FACTORY(api)
    
    with open('numpy_api_search.sql', 'w') as f: 
        f.write('#legacySQL\n')
        f.write(apq.query) 
    with open('numpy_api_count.sql','w') as f:
        f.write('#legacySQL\n')
        f.write(apq.count_query)


def build_import_query():
    """
    Construct a first pass query to detect all of the numpy imports
    """
    #TODO: implement this or AST?j
    pass

def get_npcalls(tree):
    import ast

    
    importfromlist = []
    importlist = []
    calllist = []
    
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom):
            if node.module=='numpy':
                for n in node.names:
                    importfromlist.append(n)
        elif isinstance(node, ast.Import):
            for n in node.names:
                importlist.append(n)
        elif isinstance(node,ast.Call):
            if isinstance(node.func,ast.Attribute):
                if node.func.attr in [ n.asname if n.asname else n.name for n in importfromlist ]:
                    calllist.append(node.func.attr)
                elif isinstance(node.func.value, ast.Name):
                    if node.func.value.id in [ a.asname if a.asname else a.name for a in importlist]:
                        calllist.append(node.func.value.id+'.'+node.func.attr)
            elif isinstance(node.func,ast.Name):
                if node.func.id in [ n.asname if n.asname else n.name for n in importfromlist ]:
                    calllist.append(node.func.id)
    return calllist

