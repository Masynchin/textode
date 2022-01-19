import os
from typing import List

from vkbottle import Keyboard, Text, PhotoMessageUploader
from vkbottle.bot import Bot, Message
from textode import BackNode, FuncNode, KeyboardNode, ImageNode, Node, TextNode

# from simple_node import NodeDict
# from image_node import NodeDict


bot = Bot(os.getenv("VK_TOKEN"))
image_uploader = PhotoMessageUploader(bot.api)


@bot.on.message()
async def handler(message: Message):
    node = NodeDict.get_node(message.text)
    if node is None:
        await message.answer("Couldn't recognize message text")
        return

    if isinstance(node, (FuncNode, TextNode)):
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


def make_keyboard(buttons: List[Node]) -> str:
    """Create keyboard from KeyboardNode's buttons"""
    keyboard = Keyboard(inline=False)
    for button in buttons:
        keyboard.row()
        keyboard.add(Text(button.title))

    return keyboard.get_json()


bot.run_forever()
