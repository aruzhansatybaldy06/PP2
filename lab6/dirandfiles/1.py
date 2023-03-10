import os

path = r'C:\Users\ARU\Desktop'

for i in os.listdir(path):
    if os.path.isdir(os.path.join(path,i)):
        print(i)
print('------------------------------------------------------------------\n')

for i in os.listdir(path):
    if not os.path.isdir(os.path.join(path,i)):
        print(i)

print('------------------------------------------------------------------\n')

for i in os.listdir(path):
    print(i)