import re

from textnode import TextType, TextNode
from htmlnode import LeafNode


def text_node_to_html_node(text_node):
    if not isinstance(text_node, TextNode):
        raise ValueError("TextNode should be provided as input")

    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(tag=None, value=text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", value=text_node.text, 
                            props={"href": text_node.url})
        case TextType.IMAGES:
            return LeafNode(
                tag="img",
                value="",
                props={"src": text_node.url, "alt": text_node.text}
                )
        case _:
            raise ValueError("Unsupported TextType")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes = []

    for node in old_nodes:
        if len(node) > 1:
            nodes.append(split_nodes_delimiter(node))
            continue

        splitted = node.split(delimiter)

    delimiters_type = {
        "`": TextType.CODE,
        "**": TextType.BOLD,
        "_": TextType.ITALIC
    }

    for i in range(len(splitted)):
        if i % 2 == 0:
            nodes.append(TextNode(splitted[i], text_type))         
        else:
            nodes.append(TextNode(splitted[i], delimiters_type[delimiter]))

    return nodes


def extract_markdown_images(text):
    regular_expression = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(regular_expression, text)
    return matches


def extract_markdown_links(text):
    regular_expression = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(regular_expression, text)
    return matches


def split_nodes_image(old_nodes):
    result = []

    for old_node in old_nodes:
        # Only process TEXT nodes
        if old_node.text_type != TextType.TEXT:
            result.append(old_node)
            continue

        # Check if this node has any images
        images = extract_markdown_images(old_node.text)
        if not images:
            # No images found, keep the original node
            result.append(old_node)
            continue

        # Process the text, splitting at each image
        remaining_text = old_node.text
        
        for image_alt, image_url in images:
            # Split the text at the image markdown
            parts = remaining_text.split(f"![{image_alt}]({image_url})", 1)

            # Add the text before the image if it's not empty
            if parts[0]:
                result.append(TextNode(parts[0], TextType.TEXT))

            # Add the image node
            result.append(TextNode(image_alt, TextType.IMAGES, image_url))

            # Update remaining text to be what comes after the image
            remaining_text = parts[1] if len(parts) > 1 else ""

        # Add any remaining text after the last image
        if remaining_text:
            result.append(TextNode(remaining_text, TextType.TEXT))

    return result
