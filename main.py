'''To Run'''
from python_basics.automate import list_files, download_files
from central_log import config_log

# configure logging
config_log()

TEST_URL = ("https://dataverse.harvard.edu/api/access/datafile/:"
            "persistentId?persistentId=doi:10.7910/DVN/HG7NV7/YZWKHN")

download_files(TEST_URL, "temp", ".csv")
files, file_info = list_files("temp", ".csv")
