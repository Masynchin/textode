import os
from typing import List

from aiogram import Bot, Dispatcher, executor
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types.message import Message

from textode import BackNode, FuncNode, KeyboardNode, Node, TextNode
from simple_node import NodeDict


bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher(bot=bot)


@dp.message_handler(lambda _: True)
async def handle_text(message: Message):
    """Handler of all text messages."""
    node = NodeDict.get_node(message.text)
    if node is None:
        await message.answer("Couldn't recognize message text")
        return

    if isinstance(node, (FuncNode, TextNode)):
        await message.answer(node.text)
    elif isinstance(node, KeyboardNode):
        keyboard = make_keyboard(node.buttons)
        await message.answer(node.text, reply_markup=keyboard)
    elif isinstance(node, BackNode):
        keyboard = make_keyboard(node.get_node_to_back().buttons)
        await message.answer(node.text, reply_markup=keyboard)


def make_keyboard(node_buttons: List[Node]) -> ReplyKeyboardMarkup:
    """Create keyboard from KeyboardNode's buttons"""
    return ReplyKeyboardMarkup(
        [[KeyboardButton(text=node.title)] for node in node_buttons],
        resize_keyboard=True,
    )


if __name__ == "__main__":
    executor.start_polling(dp)
