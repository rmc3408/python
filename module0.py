## Packages is collection of modules.
## and Modules is a collect of PY files scripts.


'''To connects modules (PY files in same directory).'''
## FROM [Filename.py] IMPORT [FunctionName] 
from module1 import double_num
double_num(5)


'''To Connects PaCkages(files PY in subdirectory
and MUST contain __init__.py file'''

### FROM [Directory.SubDirectory] IMPORT [Filename] 
from myPack import someMain
from myPack.subPack import someSub


someMain.main_report()
someSub.sub_report()


