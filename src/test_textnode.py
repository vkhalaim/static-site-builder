import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_n_eq(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_w_link(self):
        node = TextNode("This is a text node", TextType.LINK, "/usr/images")
        node2 = TextNode("This is a text node", TextType.LINK, "/usr/images")
        self.assertEqual(node, node2)

    def test_n_eq_w_link(self):
        node = TextNode("This is a text node", TextType.LINK, "/usr/images")
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_diff_link_text(self):
        node = TextNode("This is a text node.", TextType.LINK, "/usr/images")
        node2 = TextNode("This is a text node!", TextType.LINK, "/usr/images")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
