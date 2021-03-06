from typing import Callable, Dict, List, Optional


class Node:
    """Base class of all nodes.

    All subclasses must have this one attribute:
    - `text`: text that will be send after clicking at keyboard button.
    """

    text: str


class Keyboard(Node):
    """Keyboard node.

    This node is created for sending keyboard with its own buttons nodes.
    """

    _parent: Optional["Keyboard"] = None

    def __init__(self, text: str, buttons: Dict[str, Node]):
        self.text = text

        if not buttons:
            raise ValueError("Keyboard node must contain at least one button")

        self.buttons = buttons
        self._set_as_parent_to_buttons()

    def _set_as_parent_to_buttons(self):
        """Set parent to childs buttons.

        This required by BackNode to be able to get any level height parent.
        """
        for child in self.buttons.values():
            child._parent = self


class Text(Node):
    """Text node.

    Default node that contains text that will be sent to the user.
    """

    def __init__(self, text: str):
        self.text = text


class Func(Node):
    """Function node.

    This node behaves like a TextNode
    but `text` property generated by given func.
    """

    def __init__(self, text_func: Callable[[], str]):
        self.text_func = text_func

    @property
    def text(self):
        return self.text_func()


class Back(Node):
    """Back node.

    This node returns user back in node hierarchy.
    """

    _parent: Keyboard

    def __init__(self, text: str, level: int):
        self.text = text
        self.level = level

    def get_node_to_back(self) -> Keyboard:
        """Get "user returns to" node."""
        node = self._parent
        level = self.level
        while level:
            level -= 1
            if node._parent is None:
                return node
            node = node._parent
        return node


class Image(Node):
    """Image node.

    This node sends user an image.

    If `caption` doesn't provided, you still can pass `node.caption`
    in `message.answer_photo`.
    """

    def __init__(self, path: str, caption: Optional[str] = None):
        self.path = path
        self.caption = caption


class Multi(Node):
    """Multi node.

    This node represents multiple nodes thats need to be send at one time.
    """

    def __init__(self, nodes: List[Node]):
        self.nodes = nodes

    @property
    def _parent(self) -> Keyboard:
        """Parent property to override its setting."""

    @_parent.setter
    def _parent(self, parent: Keyboard):
        """Set provided parent for children of keyboard node type."""
        for node in self.nodes:
            if isinstance(node, Keyboard):
                node._parent = parent
