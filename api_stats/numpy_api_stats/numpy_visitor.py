import ast
import types
import inspect
from textwrap import dedent
from collections import deque

# from features import *

NUMPY_API = set()


def _compile_lib_matcher(libs):
    matches = []
    for allowed in libs:
        matches.append(allowed.replace('.', '\\.')
                              .replace('*', '.*$'))
    return r'|'.join(matches)


# ------------------------------------------------------------------------
# AST Traversal
# ------------------------------------------------------------------------

GLOBAL = 0


class NumpyVisitor(ast.NodeVisitor):

    def __init__(self, features, libs):
        self.scope = deque([('global', 0)])
        self.features = features
        self.imports = []
        self.importfroms = []
        self.calls = []

        if libs:
            self.libs = _compile_lib_matcher(libs)
        else:
            self.libs = None

    def __call__(self, source):
        if isinstance(source, types.ModuleType):
            source = dedent(inspect.getsource(source))
        if isinstance(source, types.FunctionType):
            source = dedent(inspect.getsource(source))
        if isinstance(source, types.LambdaType):
            source = dedent(inspect.getsource(source))
        elif isinstance(source, str):
            source = source
        else:
            raise NotImplementedError

        self._source = source
        self._ast = ast.parse(source)
        self.visit(self._ast)

    def visit_Import(self, node):
        for n in node.names:
            self.imports.append(n)

    def visit_ImportFrom(self, node):
        if node.module == 'numpy':
            for n in node.names:
                self.importfroms.append(n)

    def visit_Call(self, node):
        self.visit(node.func)

    def visit_Attribute(self, node):
        if node.attr in [n.asname if n.asname
                         else n.name for n in self.importfroms]:
                self.calls.append(node.attr)

    def visit_Name(self, node):
        if node.id in [n.asname if n.asname
                       else n.name for n in self.imports]:
                self.calls.append(node.id + '.' + node.func.attr)

    def get_calls(self):
        return self.calls

    def get_imports(self):
        return [n.name for n in self.imports]
    
    def get_importfroms(self):
        return [n.name for n in self.importfroms]