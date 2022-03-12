import os
from typing import List

from aiogram import Bot, Dispatcher, executor
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types.message import Message

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
bot = Bot(token=os.getenv("TG_TOKEN"))
dp = Dispatcher(bot=bot)


@dp.message_handler()
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
        await message.answer(node.text, reply_markup=keyboard)
    elif isinstance(node, Back):
        keyboard = make_keyboard(node.get_node_to_back().buttons)
        await message.answer(node.text, reply_markup=keyboard)
    elif isinstance(node, Image):
        with open(node.path, mode="rb") as image:
            await message.answer_photo(image, caption=node.caption)


def make_keyboard(buttons: List[str]) -> ReplyKeyboardMarkup:
    """Create keyboard from Keyboard's buttons."""
    return ReplyKeyboardMarkup(
        [[KeyboardButton(text=button)] for button in buttons],
        resize_keyboard=True,
    )


if __name__ == "__main__":
    executor.start_polling(dp)
