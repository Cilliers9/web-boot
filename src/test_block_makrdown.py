import unittest

from block_markdown import markdown_to_blocks, block_to_block_type, BlockType


class TestTextNode(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_striped(self):
        md = """
  This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line  

- This is a list
- with items  
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_empty_line(self):
        md = """
This is **bolded** paragraph

  

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line



- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type_heading(self):
        block = "# Heading text"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, 
                         BlockType.HEADING)

    def test_block_to_block_type_code(self):
        block = """```
Code block
```"""
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, 
                         BlockType.CODE)

    def test_block_to_block_type_quote(self):
        block = """> Quote block
> Quote block"""
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, 
                         BlockType.QUOTE)

    def test_block_to_block_type_unordered_list(self):
        block = """- List block
- List block"""
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, 
                         BlockType.UNORDERED_LIST)
        
    def test_block_to_block_type_ordered_list(self):
        block = """1. List block
2. List block"""
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, 
                         BlockType.ORDERED_LIST)
        
    def test_block_to_block_type_paragraph(self):
        block = """
`Paragraph of text
4 Paragraph of text
Paragraph of text
"""
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, 
                         BlockType.PARAGRAPH)