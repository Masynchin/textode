# textode

Textode is a simple tool to create [aiogram](https://github.com/aiogram/aiogram) text bots with only one handler.

## Installation

via pip:

`pip install textode`

or poetry:

`poetry add textode`

## Usage

Look [here](https://github.com/Masynchin/textode/tree/main/examples)
for usage examples with schemas (built by [Graphviz](https://graphviz.org/)
with [JetBrains Mono](https://www.jetbrains.com/lp/mono/) font).

**Note `NodeDict` imports**

If `my_node.py` contains your node, you must import `NodeDict` in this file, and then import `NodeDict` from `my_node.py` to file with bot. If your node and your bot are placed in one file, you only need to use `from textode import NodeDict`.
