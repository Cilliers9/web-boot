from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "P"
    HEADING = "H"
    CODE = "```"
    QUOTE = "> "
    UNORDERED_LIST = "- "
    ORDERED_LIST = "%. "

def markdown_to_blocks(markdown):
    blocks = []
    dirty_blocks = markdown.split("\n\n")
    for dirty_block in dirty_blocks:
        clean_block = dirty_block.strip()
        if clean_block != "":
            blocks.append(clean_block)
    return blocks

def block_to_block_type(block):
    if block.startswith("#"):
        return BlockType.HEADING
    elif block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE
    elif block.startswith("> "):
        lines = block.splitlines()
        every_line = True
        for line in lines:
            every_line &= line.startswith("> ")
        if every_line:
            return BlockType.QUOTE
        else:
            return BlockType.PARAGRAPH
    elif block.startswith("- "):
        lines = block.splitlines()
        every_line = True
        for line in lines:
            every_line &= line.startswith("- ")
        if every_line:
            return BlockType.UNORDERED_LIST
        else:
            return BlockType.PARAGRAPH
    elif block.startswith("1. "):
        lines = block.splitlines()
        every_line = True
        for i in range(len(lines)):
            every_line &= lines[i].startswith(f"{i+1}. ")
        if every_line:
            return BlockType.ORDERED_LIST
        else:
            return BlockType.PARAGRAPH
    else:
        return BlockType.PARAGRAPH
