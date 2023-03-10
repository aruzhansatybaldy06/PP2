for i in range(65, 65+26):
   filename = chr(i)+'.txt'
   with open(chr(i) + ".txt", "w") as file:
        file.writelines(chr(i))