__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
from zipfile import ZipFile


def clean_cache():
    path = "cache"
    if os.path.exists(path):
        for x in os.listdir(path):
            os.remove(f"{path}\{x}")
    else:
        os.mkdir("cache")


def cache_zip(zip_file_path, cache_dir_path):
    with ZipFile(zip_file_path, 'r') as zipObj:
        zipObj.extractall(cache_dir_path)


def cached_files():
    absolute_path = os.path.join(os.getcwd(), "cache")
    list_full_path = []
    for path in os.listdir(absolute_path):
        full_path = os.path.join(absolute_path, path)
        list_full_path.append(full_path)
    return list_full_path


def find_password(list):
    for x in list:
        f = open(x, "r")
        text = f.read()
        if "password" in text:
            list = text.split("\n")
            for i in list:
                if "password" in i:
                    return i[i.find(" ")+1:]
        f.close()


clean_cache()
cache_zip("data.zip", "cache")
cached_files()
find_password(cached_files())
