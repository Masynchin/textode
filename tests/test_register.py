from textode.nodes import Keyboard, Multi, Text
from textode.register import register_nodes


def test_register():
    final_node = Text("final")
    initial_node = Text("initial")
    multi_node = Multi(
        [
            Text("first"),
            Text("second"),
            Keyboard("nested keyboard", buttons={"final": final_node}),
        ]
    )
    main_node = Keyboard(
        "keyboard", buttons={"initial": initial_node, "multi": multi_node}
    )

    nodes = register_nodes(main_node, "/start")

    assert nodes.get("/start") == main_node
    assert nodes.get("initial") == initial_node
    assert nodes.get("multi") == multi_node
    assert nodes.get("final") == final_node
