'''To Run'''
from python_basics.automate import list_files, download_files
from central_log import config_log

# configure logging
config_log()

TEST_URL = "https://google.com"

download_files(TEST_URL, "temp", ".html")
files, file_info = list_files("temp", ".html")
