from textode import Image, Keyboard


main_node = Keyboard(
    "Choose image topic:",
    buttons={
        "Cats": Image("examples/image.jpg", caption="Meow"),
        "Chill": Image("examples/image.jpg"),
        "Yawn": Image("examples/image.jpg"),
    },
)
