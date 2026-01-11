from static_to_public import update_public
from generator import generate_pages_recursive
from constant import DIR_PATH_CONTENT,DEST_DIR_PATH, TEMPLATE_PATH


def main():
    
    update_public()
    generate_pages_recursive(DIR_PATH_CONTENT, TEMPLATE_PATH, DEST_DIR_PATH)

main()