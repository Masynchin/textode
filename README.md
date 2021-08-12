# textode

Textode is a simple tool to create [aiogram](https://github.com/aiogram/aiogram) text bots with only one handler.

## Usage

Look [here](https://guthub.com/Masynchin/textode/tree/main/examples) for usage examples.

Note `NodeDict` imports.
If `my_node.py` contains your node, you must import `NodeDict` in this file, and then import `NodeDict` from `my_node.py` to file with bot. If your node and your bot are placed in one file, you just need to use `from textode import NodeDict`.
