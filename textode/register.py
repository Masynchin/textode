from typing import Dict
from textode.nodes import Node, Keyboard, Multi


def register_nodes(node: Node, title: str) -> Dict[str, Node]:
    """Flat node to dict."""
    nodes = {title: node}
    if not isinstance(node, (Keyboard, Multi)):
        return nodes

    if isinstance(node, Keyboard):
        nodes = {**nodes, **_register_keyboard(node)}
    elif isinstance(node, Multi):
        for button in node.nodes:
            if isinstance(button, Keyboard):
                nodes = {**nodes, **_register_keyboard(button)}

    return nodes


def _register_keyboard(node: Keyboard) -> Dict[str, Node]:
    """Flat `Keyboard` node to dict."""
    nodes = {}
    for title, button in node.buttons.items():
        nodes = {**nodes, **register_nodes(button, title)}
    return nodes
