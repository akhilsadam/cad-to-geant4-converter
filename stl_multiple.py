#@ for multiple stl files (using folder name)
#@ input:   python stl_multiple.py <outputName> <pathToStlFolder/*.stl>

import os
import sys
import glob

fileList = glob.glob(sys.argv[2])
#print(fileList)
strlist=""
for i in fileList:
    strlist += i + " "
#print(strlist)
os.system('cmd /c "python stl_gdml.py  "'+sys.argv[1]+" "+strlist)
