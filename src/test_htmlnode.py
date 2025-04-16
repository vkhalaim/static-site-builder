import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "Paragraph text")
        node2 = HTMLNode("p", "Paragraph text")
        self.assertEqual(node, node2)

    def test_n_eq(self):
        node = HTMLNode("p", "Paragraph text")
        node2 = HTMLNode("p", "Another text")
        self.assertNotEqual(node, node2)

    def test_props_to_html_return_str(self):
        test_props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }

        node = HTMLNode("a", "Google link", props=test_props)

        self.assertEqual(type(node.props_to_html()), str)

    def test_props_to_html_return_valid_str(self):
        test_props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        expected_result = ' href="https://www.google.com" target="_blank"'

        node = HTMLNode("a", "Google link", props=test_props)

        self.assertEqual(node.props_to_html(), expected_result)

    def test_props_to_html_empty(self):
        expected_result = ""

        node = HTMLNode("a", "Google link")

        self.assertEqual(node.props_to_html(), expected_result)


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(), '<a href="https://www.google.com">Click me!</a>'
            )

    def test_leaf_to_html_img(self):
        node = LeafNode(
            "img", "Image!",
            {"href": "https://www.google.com", "alt": "Alternative text"}
            )
        self.assertEqual(
            node.to_html(),
            '<img href="https://www.google.com" alt="Alternative text">Image!</img>'
        )


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(), "<div><span>child</span></div>"
            )

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with__two_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        grandchild_node2 = LeafNode("s", "grandchild2")
        child_node = ParentNode("span", [grandchild_node, grandchild_node2])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b><s>grandchild2</s></span></div>",
        )

    def test_to_html_with_two_children(self):
        child_node = LeafNode("span", "child")
        child_node2 = LeafNode("span", "child2")
        parent_node = ParentNode("div", [child_node, child_node2])
        self.assertEqual(
            parent_node.to_html(), "<div><span>child</span><span>child2</span></div>"
            )

    def test_to_html_with_two_children_and_granchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        grandchild_node2 = LeafNode("s", "grandchild2")
        child_node = ParentNode("span", [grandchild_node])
        child_node2 = ParentNode("span", [grandchild_node2])
        parent_node = ParentNode("div", [child_node, child_node2])
        self.assertEqual(
            parent_node.to_html(), "<div><span><b>grandchild</b></span><span>"
            "<s>grandchild2</s></span></div>"
            )


if __name__ == "__main__":
    unittest.main()
