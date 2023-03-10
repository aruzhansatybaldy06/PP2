import os
p=os.listdir(r'C:\Users\ARU\Desktop\pp2\lab6\dirandfiles')

print('It exists: ', os.access(__file__, os.F_OK))
print('It is readable: ', os.access(__file__, os.R_OK))
print('It is writable: ', os.access(__file__, os.W_OK))
print('Its executable: ', os.access(__file__, os.X_OK))