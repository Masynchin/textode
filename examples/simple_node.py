from textode import BackNode, FillerNode, KeyboardNode, TextNode, TO_MAIN
from textode import NodeDict


nested_node = KeyboardNode(
    title="Yes",
    text="Here you are!",
    buttons=[
        FillerNode("Some"),
        FillerNode("Useless"),
        FillerNode("Buttons"),
        BackNode("Back to main", text="Returning to main", level=TO_MAIN),
    ],
)

nested_keyboard = KeyboardNode(
    title="Some interesting goes here...",
    text="Wanna see some nested code?",
    buttons=[
        nested_node,
        BackNode("No", text="Your choice, not mine", level=TO_MAIN),
    ],
)

help_node = TextNode(
    title="Help!",
    text="Some long and boring bot instruction...",
)

main_node = KeyboardNode(
    title="/start",
    text="Your main keyboard!",
    buttons=[
        nested_keyboard,
        help_node,
    ],
)
