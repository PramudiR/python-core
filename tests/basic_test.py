'''Unit tests for basic functions'''
import os
from datetime import datetime
from python_basics.automate import list_files


def test_list_files():
    '''test the functionality of list_files function'''
    # create temp directory and files
    temp_dir = "./test/temp"
    test_files = [
        "file1.txt",
        "file2.txt"
    ]
    for file in test_files:
        with open(os.path.join(temp_dir, file), 'w', encoding='utf-8') as f:
            f.write('')

    # expected output
    file_info = {
        "file1.txt": {
            'File size(MB)': 0,
            'Last modified': datetime.today().strftime('%d %b, %Y')
            },
        "file2.txt": {
            'File size(MB)': 0,
            'Last modified': datetime.today().strftime('%d %b, %Y')
        }
    }

    # Testing
    assert list_files(temp_dir, '.txt') == os.scandir(temp_dir), file_info
