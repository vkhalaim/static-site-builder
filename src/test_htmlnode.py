import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
