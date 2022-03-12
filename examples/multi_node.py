from textode import Image, Keyboard, Multi, Text


cats_node = Multi(
    nodes=[
        Text("Here you can see the russian cat:"),
        Image("examples/image.jpg"),
        Text("And another russian cat:"),
        Image("examples/image.jpg"),
    ],
)

main_node = Keyboard(
    "What are you looking for?",
    buttons={
        "Cars": Text("We have no article about this topic"),
        "Cats": cats_node,
        "Stars": Text("It is better to see them in the sky"),
    },
)
