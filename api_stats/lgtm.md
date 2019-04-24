<!-- The Semmle Query Language QL allows queries to be made at lgtm.com on their
query console. The language has a bit of a learning curve.
The following code snippet is able to find the imports and return the alias used
by said import. Going forward I would recommend first looking at Calls, Functions,
and FunctionCalls.-->

import python

from Import import
where import.getAnImportedModuleName() = "import"   
select import.getAName().getAsname()
