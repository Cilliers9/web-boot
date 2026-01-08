import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = TextNode("This is a text node", TextType.LINK)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_default_url(self):
        node = TextNode("This is a text node", TextType.LINK, None)
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, Plain Text, https://www.boot.dev)", repr(node)
        )

    def test_text(self):
        html_node = text_node_to_html_node(TextNode("This is a text node", TextType.TEXT))
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_bold(self):
        html_node = text_node_to_html_node(TextNode("This is a text node", TextType.BOLD))
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_idiomatic(self):
        html_node = text_node_to_html_node(TextNode("This is a text node", TextType.ITALIC))
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_code(self):
        html_node = text_node_to_html_node(TextNode("This is a text node", TextType.CODE))
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_link(self):
        html_node = text_node_to_html_node(TextNode("Google", TextType.LINK, "http:\\www.google.com"))
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Google")
        self.assertEqual(html_node.props, {"href": "http:\\www.google.com"})

    def test_text_link(self):
        html_node = text_node_to_html_node(TextNode("Alt text", TextType.IMAGE, "http:\\www.image.com"))
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "http:\\www.image.com", "alt": "Alt text"})
    

if __name__ == "__main__":
    unittest.main()