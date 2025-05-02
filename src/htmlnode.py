class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if not self.props:
            return ""

        props_string = " "

        for key, value in self.props.items():
            props_string += key + '=' + '"' + value + '" '
        # removed trailing space at the end
        return props_string[:-1]

    def __repr__(self):
        return "HTMLNode" + f"({self.tag}, {self.text_value}, \
              {self.children}, {self.props})"

    def __eq__(self, other):
        if self.tag == other.tag and self.value == other.value \
           and self.children == other.children and self.props == other.props:
            return True
        return False


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes mush have a value")
        if not self.tag:
            return self.value

        properties = self.props_to_html()

        return f"<{self.tag}"+properties+">"+self.value+f"</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Tag is required element")
        if not self.children:
            raise ValueError("Children elemts are required")

        html_parts = []

        for child in self.children:
            html_parts.append(child.to_html())

        return f"<{self.tag}>{''.join(html_parts)}</{self.tag}>"
