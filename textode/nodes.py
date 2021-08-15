from typing import Dict, List, Optional


class Node:
    """Base class of all nodes.

    All subclass must have this two attributes:
    - `title`: title that will appear at keyboard.
    - `text`: text that will be send after clicking at keyboard button.
    """

    title: str
    text: str


class KeyboardNode(Node):
    """Keyboard node.

    This node is created for sending keyboard with it own buttons nodes.
    """

    _parent: Optional["KeyboardNode"] = None

    def __init__(self, title: str, text: str, buttons: List[Node]):
        self.title = title
        self.text = text

        if not buttons:
            raise ValueError("KeyboardNode must contain at least one button")

        self.buttons = buttons
        self._add_childs_buttons_parent()

        NodeDict._register_node(self)

    def _add_childs_buttons_parent(self):
        """Set parent to childs buttons.

        This required by BackNode to be able get any level height parent.
        """
        for child in self.buttons:
            child._parent = self

    def get_child(self, node_title: str) -> Optional[Node]:
        """Get child by its title.

        Not recommended for use, but will help if
        you have non-unique title nodes.
        """
        for child in self.buttons:
            if child.title == node_title:
                return child
        return None


class TextNode(Node):
    """Text node.

    This node contain text that must sended to user after clicking
    on keyboard button.
    """

    def __init__(self, title: str, text: str):
        self.title = title
        self.text = text

        NodeDict._register_node(self)


class FillerNode(TextNode):
    """Filler node.

    This node has the same text and title and behaves like a TextNode.
    The only purpose of FillerNode is prototyping.
    """

    def __init__(self, title: str):
        super().__init__(title=title, text=title)


class BackNode(Node):
    """Back node.

    This node returns user back in node hierarchy.
    """

    _parent: KeyboardNode

    def __init__(self, title: str, text: str, level: int):
        self.title = title
        self.text = text
        self._level = level

        NodeDict._register_node(self)

    def get_node_to_back(self) -> KeyboardNode:
        """Get "user returns to" node."""
        node = self._parent
        level = self._level
        while level:
            level -= 1
            if node._parent is None:
                return node
            node = node._parent
        return node


class NodeDict:
    """Dictionary with all nodes.

    NodeDict must be used by message handler to get current node
    based on user message text.

    Nodes contained as dict pair, where key is title and value is node itself.

    !! Because of way how nodes contained, all nodes must have unique title.
    Otherwise, you can use FSM and store current KeyboardNode as parent
    and search by its childs to get correct non-unique title node.
    """

    _instance: Dict[str, Node] = {}

    @classmethod
    def _register_node(cls, node: Node):
        """Add node to all nodes dictionary."""
        cls._instance[node.title] = node

    @classmethod
    def get_node(cls, node_title: str) -> Optional[Node]:
        """Get node by node's title."""
        return cls._instance.get(node_title)
