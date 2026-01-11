import unittest
from markdown_to_htmlnode import markdown_to_htmlnode, extract_header
from htmlnode import HTMLNode, ParentNode, LeafNode


class TestTextNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_htmlnode(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_code(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_htmlnode(md)
        #print(repr(node))
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_quote(self):
        md = """
> This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,
> 
> This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,
"""

        node = markdown_to_htmlnode(md)
        #print(repr(node))
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet, This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,</blockquote></div>",
        )

    def test_unordered_list(self):
        md = """
-   Unordered list item 1
-   Unordered list item 2
"""

        node = markdown_to_htmlnode(md)
        #print(repr(node))
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Unordered list item 1</li><li>Unordered list item 2</li></ul></div>",
        )

    def test_ordered_list(self):
        md = """
1.  Ordered list item 1
2.  Ordered list item 2
"""

        node = markdown_to_htmlnode(md)
        #print(repr(node))
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>Ordered list item 1</li><li>Ordered list item 2</li></ol></div>",
        )

    def test_headings_multi_block(self):
        md = """
# Header 1

## Header 2

This is a paragraph with **bold** and _italic_ text. It includes a [link to example.com](https://www.example.com).
"""

        node = markdown_to_htmlnode(md)
        #print(repr(node))
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><h1>Header 1</h1><h2>Header 2</h2><p>This is a paragraph with <b>bold</b> and <i>italic</i> text. It includes a <a href="https://www.example.com">link to example.com</a>.</p></div>',
        )

    def test_extract_header(self):
        md = " # Header 1 Testing  "
        header = extract_header(md)
        self.assertEqual(header, "Header 1 Testing")