"""from pyunpack import Archive
import os

path = "TY 77 05 25F"

# Check whether the specified path exists or not
isExist = os.path.exists(path)
if not isExist:

   # Create a new directory because it does not exist
   os.makedirs(path)
   print("The new directory is created!")
Archive('TY 77 05 25F.rar').extractall(path)

toremove=path+".rar"
os.remove(toremove)

import shutil
import os

import shutil
import os


import pathlib
path = "./"
dir = os.listdir( path )
for file in dir:
   #print(file)
   if os.path.isdir(file):
      #print(file+"-dir")

      if len(os.listdir(path+"/"+file)) == 0: # Check if the folder is empty
         shutil.rmtree(path+"/"+file)

      dirin = os.listdir(file)

      for f in dirin:
         #print(f+"ok1")

         if f.endswith(".rar"):
            print(f+"ok")
            x=f.split(".")[0]
            print(x)
            if not(os.path.exists("./"+file+"/"+x+"-extracted")):
                os.makedirs("./"+file+"/"+x+"-extracted")
                Archive("./"+file+"/"+f).extractall("./"+file+"/"+x+"-extracted")
                os.remove("./"+file+"/"+f)
"""
import os
from pyunpack import Archive
tree = os.walk('./')
#print(tree)

for i in tree:
    curdir=i[0]
    subdirslist=i[1]
    subfileslist=i[2]
    for x in i[2]:
         if x.endswith(".rar"):
            y=x.split(".")[0]
            if not( os.path.exists(os.path.join(i[0],y+"-extracted2"))    ):
                try:
                    os.makedirs(os.path.join(i[0],y+"-extracted2"))
                    Archive(os.path.join(curdir,x)).extractall(os.path.join(i[0],y+"-extracted2"))
                    os.remove(curdir+"/"+x)
                except :
                    print("ok")














