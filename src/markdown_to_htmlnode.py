from block_markdown import markdown_to_blocks, block_to_block_type, BlockType
from htmlnode import ParentNode, LeafNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

def paragraph_to_children(block):
    line = block.replace("\n", " ")
    children = []
    text_nodes = text_to_textnodes(line)
    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))
    return children

def quote_to_children(block):
    lines = block.splitlines()
    children = []
    quote = ""
    for line in lines:
        if line == "> ":
            continue
        quote += f"{line.removeprefix("> ")} "
    text_nodes = text_to_textnodes(quote.rstrip())
    for text_node in text_nodes:
            children.append(text_node_to_html_node(text_node))
    return children

def list_to_children(block):
    lines = block.splitlines()
    children = []
    for line in lines:
        prefix = line.split(maxsplit=1)
        text_nodes = text_to_textnodes(prefix[1])
        grandchildren = []
        for text_node in text_nodes:
            grandchildren.append(text_node_to_html_node(text_node))
        children.append(ParentNode("li", grandchildren))
    return children

def block_to_htmlnode(block, block_type):
    match(block_type):
        case BlockType.PARAGRAPH:
            children = paragraph_to_children(block)
            div_child = ParentNode("p", children)
        case BlockType.HEADING:
            level = block.split(maxsplit=1)
            children = paragraph_to_children(level[1])
            div_child = ParentNode(f"h{len(level[0])}", children)
        case BlockType.CODE:
            code = block.removeprefix("```\n").removesuffix("```")
            pre_child = LeafNode("code", code)
            div_child = ParentNode("pre", [pre_child])
        case BlockType.QUOTE:
            children = quote_to_children(block)
            div_child = ParentNode("blockquote", children)
        case BlockType.UNORDERED_LIST:
            children = list_to_children(block)
            div_child = ParentNode("ul", children)
        case BlockType.ORDERED_LIST:
            children = list_to_children(block)
            div_child = ParentNode("ol", children)
    return div_child


def markdown_to_htmlnode(markdown):
    blocks = markdown_to_blocks(markdown)
    div_children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        div_children.append(block_to_htmlnode(block, block_type))
    html_node = ParentNode("div", div_children)
    return html_node