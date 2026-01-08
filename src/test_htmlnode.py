import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestTextNode(unittest.TestCase):

    def test_default(self):
        node = HTMLNode()
        node2 = HTMLNode(tag=None, value=None, children=None, props=None)
        self.assertEqual(node, node2)

    def test_eq(self):
        node = HTMLNode("p", "This is a text node", ["Node","Node2"], {"href":"link", "target": "_blank"})
        node2 = HTMLNode(tag="p", value="This is a text node", children=["Node","Node2"], props={"href":"link", "target": "_blank"})
        self.assertEqual(node, node2)
    
    def test_props_html(self):
        node = HTMLNode(props={
            "href": "https://www.google.com",
            "target": "_blank",
            })
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_props_html(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), '')

    def test_repr(self):
        node = HTMLNode("a", "HTML value text", ["child", "child2"], {"href": "https://www.boot.dev", "target": "_blank"})
        string = '''HTMLNode(a, \nHTML value text, \n['child', 'child2'], \n{'href': 'https://www.boot.dev', 'target': '_blank'})'''
        self.assertMultiLineEqual(repr(node), string)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_promp(self):
        node1 = LeafNode("a", "Click me!", props={"href": "https://www.google.com"})
        self.assertEqual(node1.props, {"href": "https://www.google.com"})
        self.assertEqual(node1.props_to_html(), ' href="https://www.google.com"')
        self.assertEqual(node1.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_no_tag(self):
        node2 = LeafNode(None, "Hello, world!")
        self.assertEqual(node2.to_html(), "Hello, world!")

    def test_to_html_with_child(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_children(self):
        parent_node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(parent_node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
    

    def test_to_html_with_grandchild(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_grandchildren(self):
        grandchild_node2 = LeafNode("i", "grandchild2")
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("p", [grandchild_node, grandchild_node2])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><p><b>grandchild</b><i>grandchild2</i></p></div>",
        )

    def test_to_html_with_children_and_props(self):
        parent_node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            {"href": "text"}
        )
        self.assertEqual(parent_node.to_html(), '<p href="text"><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')
    


if __name__ == "__main__":
    unittest.main()