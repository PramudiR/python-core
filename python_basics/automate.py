# Automate tasks with Python
import os
from shutil import move
import logging

from data_science.time_data import seconds2Date

# Identify fie types
def fileIdentifier(filepath):
    extension = os.path.splitext(filepath)[1]
    
    # supported image types
    image_extensions = [".jpg", ".jpeg", ".jif", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", 
                        ".raw", ".arw", ".cr2", ".nrw", ".k25", ".bmp", ".dib", ".heif", ".heic", 
                        ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
    # supported Video types
    video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                        ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]
    # supported Audio types
    audio_extensions = [".m4a", ".flac", ".mp3", ".wav", ".wma", ".aac"]
    # supported Document types
    document_extensions = [".doc", ".docx", ".odt",
                        ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]
    
    # Map extensions to their categories
    extension_categories = {
        **{ext: 'image' for ext in image_extensions},
        **{ext: 'video' for ext in video_extensions},
        **{ext: 'audio' for ext in audio_extensions},
        **{ext: 'document' for ext in document_extensions}
    }

    return extension_categories.get(extension.lower(), 'other')

# Sort files in a given directory
def sortFiles(dirPath: str):
    if not os.path.isdir(dirPath):
        logging.info(f"{dirPath} does not exists")
        return None
    
    for entry in os.scandir(dirPath):
        if entry.is_file():
            category = fileIdentifier(entry.name)
            subdir = os.path.join(dirPath, category)
            os.makedirs(subdir, exist_ok=True)
            move(entry.path, os.path.join(subdir, entry.name))
        
    return(f"{dirPath} scanned successfully")

# Get the list of given file type from a directory 
def listFiles(dirPath: str, fileType: str):
    if not os.path.isdir(dirPath):
        logging.info(f"{dirPath} does not exists")
        return (None, None)
    
    files = []
    file_info  = {}

    for entry in os.scandir(dirPath):
        if entry.is_file() and (os.path.splitext(entry.name)[1] == fileType):
            files.append(entry)
            file_stat = entry.stat()
            file_info[entry.name] = {
                "File size(MB)": (file_stat.st_size/(1024*1024)),
                "Last modified": seconds2Date(file_stat.st_mtime)
                }
    
    return files, file_info

'''
A DirEntry object in Python's os module represents an entry in a directory, 
and it provides several properties that you can use to access information about the entry. 
Some of the commonly used properties include:

name: The name of the entry (file or directory).
path: The full path to the entry.
is_dir(): Method that returns True if the entry is a directory.
is_file(): Method that returns True if the entry is a regular file.
is_symlink(): Method that returns True if the entry is a symbolic link.
stat(): Method that returns an os.stat_result object with information about the entry, such as size, permissions, and timestamps.

'''