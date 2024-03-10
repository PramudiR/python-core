# Automate tasks with Python
from os import path, scandir, makedirs
from shutil import move


def fileIdentifier(filepath):
    extension = path.splitext(filepath)[1]
    
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


def sortFiles(dirPath: str):
    if not path.isdir(dirPath):
        return(f"{dirPath} does not exists")
    
    for entry in scandir(dirPath):
        if entry.is_file():
            category = fileIdentifier(entry.name)
            subdir = path.join(dirPath, category)
            makedirs(subdir, exist_ok=True)
            move(entry.path, path.join(subdir, entry.name))
        
    return(f"{dirPath} scanned successfully")