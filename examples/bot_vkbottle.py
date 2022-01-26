import os
from typing import List

from vkbottle import Keyboard, Text, PhotoMessageUploader
from vkbottle.bot import Bot, Message
from textode import (
    BackNode,
    FuncNode,
    KeyboardNode,
    ImageNode,
    MultiNode,
    Node,
    TextNode,
)

# from simple_node import NodeDict
# from image_node import NodeDict
# from multi_node import NodeDict


bot = Bot(os.getenv("VK_TOKEN"))
image_uploader = PhotoMessageUploader(bot.api)


@bot.on.message()
async def handle_message(message: Message):
    """Handler of all messages."""
    node = NodeDict.get_node(message.text)
    if node is None:
        await message.answer("Couldn't recognize message text")
    else:
        await handle_node(node, message)


async def handle_node(node: Node, message: Message):
    """Answer to message depends on node's type."""
    if isinstance(node, MultiNode):
        for node in node.nodes:
            await handle_node(node, message)
    elif isinstance(node, (FuncNode, TextNode)):
        await message.answer(node.text)
    elif isinstance(node, KeyboardNode):
        keyboard = make_keyboard(node.buttons)
        await message.answer(node.text, keyboard=keyboard)
    elif isinstance(node, BackNode):
        keyboard = make_keyboard(node.get_node_to_back().buttons)
        await message.answer(node.text, keyboard=keyboard)
    elif isinstance(node, ImageNode):
        with open(node.path, mode="rb") as f:
            attachment = await image_uploader.upload(f.read())
        await message.answer(node.caption, attachment=attachment)


def make_keyboard(node_buttons: List[Node]) -> str:
    """Create keyboard from KeyboardNode's buttons."""
    keyboard = Keyboard(inline=False)
    for node in node_buttons:
        keyboard.row()
        keyboard.add(Text(node.title))

    return keyboard.get_json()


if __name__ == "__main__":
    bot.run_forever()
