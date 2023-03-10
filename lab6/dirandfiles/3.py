import os
p=(r'C:\Users\ARU\Desktop\pp2\lab6\dirandfiles')

if os.path.exists(p):
    print("filename and directory portion of the given path")
    print(os.path.basename(p))
    print(os.path.dirname(p))
else:
    print("Doesnt exist")