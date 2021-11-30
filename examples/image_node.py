from textode import ImageNode, KeyboardNode
from textode import NodeDict


main_node = KeyboardNode(
    title="/start",
    text="Choose image topic:",
    buttons=[
        ImageNode(title="Cats", path="examples/image.jpg", caption="Meow"),
        ImageNode(title="Chill", path="examples/image.jpg"),
        ImageNode(title="Yawn", path="examples/image.jpg"),
    ],
)
