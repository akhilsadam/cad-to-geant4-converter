#@ for multiple stl files (using folder name)
#@ input:   python stl_multiple.py  relativePathToStlFolder/*.stl

import glob
import sys

fileList = glob.glob(sys.argv[1])
print(fileList)
