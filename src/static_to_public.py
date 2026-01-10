import os
import shutil

def update_public():
    public_dir = os.path.abspath("./public")
    static_dir = os.path.abspath("./static")
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
    os.mkdir(public_dir)
    copy_static_to_public(static_dir, public_dir)


def copy_static_to_public(source, destination):
    source_dir_sub = os.listdir(source)
    print(source_dir_sub)
    if len(source_dir_sub) == 0:
        return
    for sub in source_dir_sub:
        print(sub)
        sub_source = os.path.join(source, sub)
        desti_path = os.path.join(destination, sub)
        if os.path.isfile(sub_source):
            shutil.copy(sub_source, destination)
        elif os.path.isdir(sub_source):
            os.makedirs(desti_path)
            copy_static_to_public(sub_source, desti_path)