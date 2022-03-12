import os
from typing import List

from vkbottle import (
    Keyboard as VkKeyboard,
    Text as VkText,
    PhotoMessageUploader,
)
from vkbottle.bot import Bot, Message
from textode import (
    register_nodes,
    Back,
    Func,
    Keyboard,
    Image,
    Multi,
    Node,
    Text,
)

# from simple_node import main_node
# from image_node import main_node
# from multi_node import main_node


nodes = register_nodes(main_node, "/start")
bot = Bot(os.getenv("VK_TOKEN"))
image_uploader = PhotoMessageUploader(bot.api)


@bot.on.message()
async def handle_message(message: Message):
    """Handler of all messages."""
    node = nodes.get(message.text)
    if node is None:
        await message.answer("Couldn't recognize message text")
    else:
        await handle_node(node, message)


async def handle_node(node: Node, message: Message):
    """Answer to message depends on node's type."""
    if isinstance(node, Multi):
        for node in node.nodes:
            await handle_node(node, message)
    elif isinstance(node, (Func, Text)):
        await message.answer(node.text)
    elif isinstance(node, Keyboard):
        keyboard = make_keyboard(node.buttons.keys())
        await message.answer(node.text, keyboard=keyboard)
    elif isinstance(node, Back):
        keyboard = make_keyboard(node.get_node_to_back().buttons)
        await message.answer(node.text, keyboard=keyboard)
    elif isinstance(node, Image):
        with open(node.path, mode="rb") as f:
            attachment = await image_uploader.upload(f.read())
        await message.answer(node.caption, attachment=attachment)


def make_keyboard(buttons: List[str]) -> str:
    """Create keyboard from Keyboard's buttons."""
    keyboard = VkKeyboard(inline=False)
    for button in buttons:
        keyboard.row()
        keyboard.add(VkText(button))

    return keyboard.get_json()


if __name__ == "__main__":
    bot.run_forever()
