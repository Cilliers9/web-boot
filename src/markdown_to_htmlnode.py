from block_markdown import markdown_to_blocks, block_to_block_type, BlockType
from htmlnode import ParentNode

def markdown_to_html(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        
        match(block_to_block_type(block)):
            case BlockType.PARAGRAPH:
                