import pytest

from textode.constants import TO_MAIN
from textode.nodes import (
    BackNode,
    FillerNode,
    FuncNode,
    ImageNode,
    KeyboardNode,
    MultiNode,
    TextNode,
)


def test_text_node():
    node = TextNode(title="title", text="text")
    assert node.title == "title"
    assert node.text == "text"


def test_filler_node():
    node = FillerNode("both_title_and_text")
    assert node.title == node.text == "both_title_and_text"


def test_func_node():
    number = 0

    def text_func():
        nonlocal number
        number += 1
        return str(number)

    node = FuncNode(title="title", text_func=text_func)
    assert node.title == "title"

    assert node.text == "1"
    assert node.text == "2"
    assert node.text == "3"


def test_keyboard_node():
    with pytest.raises(ValueError):
        KeyboardNode(title="title", text="text", buttons=[])

    titles = ("one", "two", "three")
    buttons = [FillerNode(title) for title in titles]
    node = KeyboardNode(title="title", text="text", buttons=buttons)

    assert node.title == "title"
    assert node.text == "text"
    assert node.buttons == buttons

    for button, title in zip(node.buttons, titles):
        assert button.title == button.text == title


def test_back_node():
    back_node = BackNode(
        title="go back", text="returning to ...", level=TO_MAIN
    )

    nested_keyboard = KeyboardNode(
        title="title", text="text", buttons=[back_node]
    )
    main_keyboard = KeyboardNode(
        title="title", text="text", buttons=[nested_keyboard]
    )

    assert back_node.get_node_to_back() == main_keyboard


def test_image_node():
    image_node = ImageNode(title="title", path="image.png", caption="caption")
    assert image_node.title == "title"
    assert image_node.caption == "caption"
    assert image_node.path == "image.png"

    without_caption = ImageNode(title="title", path="image.png")
    assert without_caption.caption is None


def test_multi_node():
    title = "title"
    children = [FillerNode(title), TextNode(title=title, text="text")]
    multi_node = MultiNode(title=title, nodes=children)
    assert multi_node.title == title
    assert multi_node.nodes == children
