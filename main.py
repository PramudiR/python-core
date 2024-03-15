'''To test the use cases of different functions'''
from python_basics.automate import list_files

files, file_info = list_files(".", ".md")
print(file_info)
