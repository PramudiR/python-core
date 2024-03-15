''' Automate tasks with Python '''
import os
from shutil import move
import logging

from data_science.time_data import seconds_2_date


def file_identifier(filepath: str) -> str:
    '''Identify fie types'''
    extension = os.path.splitext(filepath)[1]

    # supported image types
    image_extensions = [".jpg", ".jpeg", ".jif", ".png", ".gif", ".webp",
                        ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2",
                        ".nrw", ".k25", ".bmp", ".dib", ".heif", ".heic",
                        ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm",
                        ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
    # supported Video types
    video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv",
                        ".ogg", ".mp4", ".mp4v", ".m4v", ".avi", ".wmv",
                        ".mov", ".qt", ".flv", ".swf", ".avchd"]
    # supported Audio types
    audio_extensions = [".m4a", ".flac", ".mp3", ".wav", ".wma", ".aac"]
    # supported Document types
    document_extensions = [".doc", ".docx", ".odt", ".pdf", ".xls", ".xlsx",
                           ".ppt", ".pptx"]

    # Map extensions to their categories
    extension_categories = {
        **{ext: 'image' for ext in image_extensions},
        **{ext: 'video' for ext in video_extensions},
        **{ext: 'audio' for ext in audio_extensions},
        **{ext: 'document' for ext in document_extensions}
    }

    return extension_categories.get(extension.lower(), 'other')


def sort_files(dir_path: str) -> str:
    '''Sort files in a given directory'''
    if not os.path.isdir(dir_path):
        logging.info("Path not exist: %s", dir_path)
        return None

    for entry in os.scandir(dir_path):
        if entry.is_file():
            category = file_identifier(entry.name)
            subdir = os.path.join(dir_path, category)
            os.makedirs(subdir, exist_ok=True)
            move(entry.path, os.path.join(subdir, entry.name))

    return f"{dir_path} scanned successfully"


def list_files(
        dir_path: str,
        file_type: str
        ) -> (tuple[None, None] | tuple[list, dict]):
    '''Get the list of given file type from a directory'''

    if not os.path.isdir(dir_path):
        logging.info("Path not exist: %s", dir_path)
        return (None, None)

    files = []
    file_info = {}

    for entry in os.scandir(dir_path):
        if entry.is_file() and (os.path.splitext(entry.name)[1] == file_type):
            files.append(entry)
            file_stat = entry.stat()
            file_info[entry.name] = {
                "File size(MB)": (file_stat.st_size/(1024*1024)),
                "Last modified": seconds_2_date(file_stat.st_mtime)
                }

    return files, file_info
