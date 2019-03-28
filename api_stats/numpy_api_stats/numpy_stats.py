from google.cloud import bigquery
import numpy as np
from pandas import read_csv as pd_read_csv
from pandas import DataFrame

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

def build_api_list(api,typelist=['module','float','function','int','ufunc']):
    

    api_list = [(x[0],x[1].__name__) for x in api]
    df_api = DataFrame(api_list,columns = ['label','type'])

    df_api.set_index('type',inplace=True)

    df_api_list = df_api.loc[typelist].reset_index()
    return [ (r[1].label,r[1].type) for r in df_api_list.iterrows()]

class API_QUERY_FACTORY:
    _typelist = ['module','function','float','int','ufunc']
    def __init__(self,api,typelist=None,content_table=None,file_table=None):
        self.api = api
        #self.api = [(x, type(np.__getattribute__(x))) for x in dir(np) if not x.startswith('__')]
        
        if  typelist: self._typelist=typelist
        else: typelist=self._typelist

        api_list = build_api_list(api,typelist)

        if content_table: self.content_table=content_table
        else: self.content_table = '[bigquery-public-data:github_repos.contents]'

        if file_table: self.file_table=file_table
        else: self.file_table = '[bigquery-public-data:github_repos.files]'

        self.query =  build_numpyAPI_query(
                                    api_list,content_table = nest_table(
                                        build_py_content(content_table_name=self.content_table,
                                                        join=join_py(file_table = self.file_table))
                                    )) 

    
# def find_types(l):
#     ''' find the types of some list of names/labels '''
#     return [(x,type( np.__getattribute__(x))) for x in l ]

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

def plot_results(results,filename='results.svg'):
    import matplotlib.pyplot as plt; plt.rcdefaults()
    import matplotlib.pyplot as plt
    
    r = results.T
    r2 = r.loc[r[0]>0].sort_values(0,ascending=False)
    r2.index = [ f.split('_')[1] for f in list(r2.index)]

    r2 = r2[:100]
    y_pos = np.arange(len(r2))
    calls = r2[0]
    
    fig1 = plt.bar(y_pos, calls, align='center', alpha=0.5,log=True)
    plt.xticks(y_pos,r2.index,rotation='vertical',fontsize=4)
    plt.ylabel('Calls')
    plt.title('API calls from github query')

    fig1 = plt.gcf() 
    plt.show()

    fig1.savefig(filename, dpi=500)

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
) '''
    return '\n'.join(['SELECT', '*', 'FROM',file_table + ' AS f','WHERE',w1string])

def nest_table(t):
    return '('+t+')'

def build_py_content(content_table_name='[bigquery-public-data:github_repos.sample_contents]',join=''):
    return '\n'.join(['SELECT','*','FROM',content_table_name + ' AS c',join])

def join_py(file_table = '[bigquery-public-data:github_repos.sample_files]'):
    return '\n'.join(['INNER JOIN',nest_table(build_py_query(file_table = file_table))+' AS p','ON','c.id = p.id'])

def get_numpyAPI_function_list(client):
    query_job = client.query( build_getAPItable_query() )  # API request
    df = query_job.result().to_dataframe()
    return [r[1][0] for r in df.iterrows()]


def detect_fun(f):
    return  f'(np\.|numpy\.){f}\(\s?[A-Za-z0-9_.\(\)]*\s?\)'

def detect_mod(m):
    return f'(import\s+numpy\.|from numpy\.{m}\s+'+'import\s+[a-zA-Z0-9_]+)'

def detect_float(f):
    return  f'(np\.|numpy\.){f}\s*[\*\+\-\/]?'

def detect_int(f):
    return  f'(np\.|numpy\.){f}'

def detect_ufunc(f):
    return f'(np\.|numpy\.){f}\(\s?[A-Za-z0-9_.\(\)]*\s?\)'

def build_cname(name,ttype):
    return '_'.join(['numpy',ttype,name])

def build_sql_regex(name,ttype, source_name = 'c.content'):
    if ttype=='function':
        return f'REGEXP_MATCH( {source_name},\'{detect_fun(name)}\' ) AS {build_cname(name,ttype)}' 
    
    elif ttype=='module':
        return f'REGEXP_MATCH({source_name},\'{detect_mod(name)}\' ) AS {build_cname(name,ttype)}'
    
    elif ttype=='float':
        return f'REGEXP_MATCH({source_name},\'{detect_float(name)}\' ) AS {build_cname(name,ttype)}'
    
    elif ttype=='int':
        return f'REGEXP_MATCH({source_name},\'{detect_int(name)}\' ) AS {build_cname(name,ttype)}'

    elif ttype=='ufunc':
        return f'REGEXP_MATCH({source_name},\'{detect_ufunc(name)}\' ) AS {build_cname(name,ttype)}'
    else:
        raise NotImplementedError 

def build_numpyAPI_query(api_list, content_table = '[bigquery-public-data:github_repos.sample_contents]'):
    qlist=[]
    source_name = 'c.content'
    for f in api_list:
        qlist.append(build_sql_regex(f[0],f[1]))
    
    return '\n'.join(['SELECT',',\n'.join(qlist),f'FROM {content_table}'])

# def build_numpyAPI_query(funlist=['abs'],modlist=['linalg'], content_table = '[bigquery-public-data:github_repos.sample_contents]'):
#     qlist=[]
#     source_name = 'c.content'
#     for f in funlist:
#         qlist.append(f'REGEXP_MATCH( {source_name},' + r"r'"+  f'(np\.|numpy\.){f}\\(' + r"\s?[A-Za-z0-9_.\(\)]*\s?\)') AS " + f'numpy_{f}')
#     for m in modlist:
#         qlist.append(f'REGEXP_MATCH( {source_name},' + r"r'"+ f'(import numpy\.|from numpy\.){m}'+'import\s+'+') AS ' + f'numpy_{f}')

#     return '\n'.join(['SELECT',',\n'.join(qlist),f'FROM {content_table}'])

def build_countAPIs(api_list,api_table='None'):
    return 'SELECT\n'+',\n'.join([f'count(CASE WHEN numpy_{f} THEN 1 END) AS {f}_count' for f in api_list]) + f'\nFROM {api_table}'

if __name__ == '__main__':
   
    import os 

    os.environ['GOOGLE_APPLICATION_CREDENTIALS']='/Users/mpeaton/Downloads/apt-footing-235018-aeb185ac9e31.json' 
    api = [(x, type(np.__getattribute__(x))) for x in dir(np) if not x.startswith('__')] 
    
    apq = API_QUERY_FACTORY(api)
    query = apq.query
    # query = build_countAPIs(funlist=apq.funs,api_table=
    #                         nest_table(
    #                             build_numpyAPI_query(
    #                                 funlist=apq.funs,content_table = nest_table(
    #                                     build_py_content(content_table_name='[bigquery-public-data:github_repos.contents]',
    #                                                     join=join_py(file_table = '[bigquery-public-data:github_repos.files]'))
    #                                 ))))    
    
    with open('numpy_api_search.sql', 'w') as f: 
        f.write(query) 

