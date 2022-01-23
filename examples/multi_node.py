from textode import ImageNode, KeyboardNode, MultiNode, TextNode
from textode import NodeDict


# MultiNode children should have the same title,
# so it could be done with walrus operator.
# You can also duplicate it without using walrus.
cats_node = MultiNode(
    title=(_ := "Cats"),
    nodes=[
        TextNode(_, text="Here you can see the russian cat:"),
        ImageNode(_, path="examples/image.jpg"),
        TextNode(_, text="And another russian cat:"),
        ImageNode(_, path="examples/image.jpg"),
    ],
)

main_node = KeyboardNode(
    title="/start",
    text="What are you looking for?",
    buttons=[
        TextNode(title="Cars", text="We have no article about this topic"),
        cats_node,
        TextNode(title="Stars", text="It is better to see them in the sky"),
    ],
)
