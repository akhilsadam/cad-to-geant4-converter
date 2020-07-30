#@ for multiple stl files (using folder name)
#@ input:   python stl_multiple.py  /pathToStlFolder/*.stl

import glob
import sys

fileList = glob.glob(sys.argv)
print(fileList)
