import os
import shutil
from constant import PUBLIC_DIR, STATIC_DIR

def update_public():
    if os.path.exists(PUBLIC_DIR):
        shutil.rmtree(PUBLIC_DIR)
    os.mkdir(PUBLIC_DIR)
    copy_static_to_public(STATIC_DIR, PUBLIC_DIR)


def copy_static_to_public(source, destination):
    source_dir_sub = os.listdir(source)
    if len(source_dir_sub) == 0:
        return
    for sub in source_dir_sub:
        sub_source = os.path.join(source, sub)
        desti_path = os.path.join(destination, sub)
        if os.path.isfile(sub_source):
            shutil.copy(sub_source, destination)
        elif os.path.isdir(sub_source):
            os.makedirs(desti_path)
            copy_static_to_public(sub_source, desti_path)