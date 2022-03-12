import pytest

from textode.constants import TO_MAIN
from textode.nodes import Back, Func, Image, Keyboard, Multi, Text


def test_text_node():
    assert Text("text").text == "text"


def test_func_node():
    number = 0

    def text_func():
        nonlocal number
        number += 1
        return str(number)

    node = Func(text_func)

    assert node.text == "1"
    assert node.text == "2"
    assert node.text == "3"


def test_keyboard_node():
    with pytest.raises(ValueError):
        Keyboard("text", buttons=[])

    titles = ("one", "two", "three")
    texts = ("four", "five", "six")
    nodes = [Text(text) for text in texts]
    buttons = dict(zip(titles, nodes))
    node = Keyboard("text", buttons=buttons)

    assert node.text == "text"
    assert node.buttons == buttons

    for button, text in zip(node.buttons.values(), texts):
        assert button.text == text


def test_back_node():
    back_node = Back("returning to ...", level=TO_MAIN)
    nested_keyboard = Keyboard("text", buttons={"go back": back_node})
    main_keyboard = Keyboard("text", buttons={"title": nested_keyboard})

    assert back_node.get_node_to_back() == main_keyboard


def test_image_node():
    image_node = Image("image.png", caption="caption")
    assert image_node.caption == "caption"
    assert image_node.path == "image.png"

    without_caption = Image("image.png")
    assert without_caption.caption is None


def test_multi_node():
    children = [Text("title"), Text("text")]
    multi_node = Multi(children)
    assert multi_node.nodes == children


def test_back_node_works_with_multi_node():
    back_node = Back("back", level=TO_MAIN)
    multi_node = Multi([Keyboard("text", buttons={"back": back_node})])
    main_node = Keyboard("text", buttons={"transparent": multi_node})

    assert back_node.get_node_to_back() == main_node
