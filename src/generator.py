import os
from markdown_to_htmlnode import markdown_to_htmlnode, extract_header

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, mode="r") as md_file:
        markdown = md_file.read()
    with open(template_path, mode="r") as html_file:
        html_template = html_file.read()
    html_nodes = markdown_to_htmlnode(markdown)
    html_string = html_nodes.to_html()
    header = extract_header(markdown)
    html = html_template.replace("{{ Title }}", header).replace("{{ Content }}", html_string).replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')

    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    with open(dest_path, mode="w") as index_file:
        write_result = index_file.write(html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    if not os.path.isdir(dir_path_content):
        raise Exception("Error: Content directory not pointing to valid directory")
    file_list = os.listdir(dir_path_content)
    for file in file_list:
        file_path = os.path.join(dir_path_content, file)
        if os.path.isdir(file_path):
            dest_file_path = os.path.join(dest_dir_path, file)
            generate_pages_recursive(file_path, template_path, dest_file_path, basepath)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file)
            dest_file_path = os.path.join(dest_dir_path, f"{file_ext[0]}.html")
            if file_ext[1] == ".md":
                generate_page(file_path, template_path, dest_file_path, basepath)