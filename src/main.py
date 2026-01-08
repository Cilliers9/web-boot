from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    
    textnode = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(repr(textnode))

    htmlnode = HTMLNode("a", "HTML value text", ["child", "child2"], {"href": "https://www.boot.dev", "target": "_blank"})
    print(repr(htmlnode))

    print(htmlnode.props_to_html())

main()