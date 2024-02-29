import os

filename = 'exaple.txt'
abs_path = os.getcwd()
file_path = os.path.join(abs_path, 'files', filename)

try:
    file = open(file_path, 'r')
except FileNotFoundError:
    print('File Not Found')
else:
    print(file.read())
    file.close()
