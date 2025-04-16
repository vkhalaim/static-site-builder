class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
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
