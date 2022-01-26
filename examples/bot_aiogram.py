import os
from typing import List

from aiogram import Bot, Dispatcher, executor
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types.message import Message

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


bot = Bot(token=os.getenv("TG_TOKEN"))
dp = Dispatcher(bot=bot)


@dp.message_handler()
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
        await message.answer(node.text, reply_markup=keyboard)
    elif isinstance(node, BackNode):
        keyboard = make_keyboard(node.get_node_to_back().buttons)
        await message.answer(node.text, reply_markup=keyboard)
    elif isinstance(node, ImageNode):
        with open(node.path, mode="rb") as image:
            await message.answer_photo(image, caption=node.caption)


def make_keyboard(node_buttons: List[Node]) -> ReplyKeyboardMarkup:
    """Create keyboard from KeyboardNode's buttons."""
    return ReplyKeyboardMarkup(
        [[KeyboardButton(text=node.title)] for node in node_buttons],
        resize_keyboard=True,
    )


if __name__ == "__main__":
    executor.start_polling(dp)
