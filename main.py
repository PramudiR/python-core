# To test the use cases of different functions
from python_basics.automate import listFiles

files, file_info = listFiles(".", ".md")
print(file_info)