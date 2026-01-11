import sys
from static_to_public import update_public
from generator import generate_pages_recursive
from constant import DIR_PATH_CONTENT,DEST_DIR_PATH, TEMPLATE_PATH


def main():
    
    if sys.argv[0] == "":
        basepath = "/"
    else:
        basepath = sys.argv[0]
    update_public()
    generate_pages_recursive(DIR_PATH_CONTENT, TEMPLATE_PATH, DEST_DIR_PATH, basepath)

main()